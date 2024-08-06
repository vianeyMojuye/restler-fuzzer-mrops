# Copyright (c) Eunice Vianey Mojuye Toukam.

from __future__ import print_function

from checkers.checker_base import *

from checkers.checker_base import *
from engine.bug_bucketing import BugBuckets
from engine.fuzzing_parameters.fuzzing_utils import *

import engine.primitives as primitives
from utils.logger import raw_network_logging as RAW_LOGGING
import json

import engine.dependencies as dependencies
from engine.core.request_utilities import NO_TOKEN_SPECIFIED
from engine.core.request_utilities import NO_SHADOW_TOKEN_SPECIFIED


STATIC_OAUTH_TOKEN = 'static_oauth_token'




class MropEquivalenceChecker(CheckerBase):
    """ Checker For Equivalence MROP Operation """

    
    def __init__(self, req_collection, fuzzing_requests):
        CheckerBase.__init__(self, req_collection, fuzzing_requests)
      


    def apply(self, rendered_sequence, lock):
        """ Applies check for fuzzing request payload body

        @param rendered_sequence: Object containing the rendered sequence information
        @type  rendered_sequence: RenderedSequence
        @param lock: Lock object used to sync more than one fuzzing job
        @type  lock: thread.Lock
        @param equivalence_post_codes: List of responds related to POST and DELETE requests 
        @type  lock: list os string

        @return: None
        @type  : None

        """
        if not rendered_sequence.valid:
            return
        self._sequence = rendered_sequence.sequence
        self._lock = lock
        self._custom_mutations = self._req_collection.candidate_values_pool.candidate_values

        # print("\n ********** self._custom_mutations :***********: \t",  self._custom_mutations)
        self._authentication_method = self._get_authentication_method()
        # print("\n **********auth***********: \t", self._authentication_method)
        if self._authentication_method not\
            in [STATIC_OAUTH_TOKEN, primitives.REFRESHABLE_AUTHENTICATION_TOKEN]:
            print("\n **********nothing*********** \n")
            return
        
        

        # if self._sequence.last_request.method.startswith('POST') or self._sequence.last_request.method.startswith('DELETE')or self._sequence.last_request.method.startswith('PUT'):
        
            # print("1- We're In _equivalence_post_and_delete_same_user \n")
            # input("enter qlq chose :\n")
        self._render_last_request(self._sequence)
            
        # python ../build-restler.py --dest_dir restler_bin                 
        # ..\restler_bin\restler\Restler.exe compile --api_spec swagger.json
        # ..\restler_bin\restler\Restler.exe fuzz-lean --grammar_file "Compile\grammar.py" --dictionary_file "Compile\dict.json" --settings "Compile\engine_settings.json" --no_ssl  --disable_checkers MropEqualityDisjoint

   
            


    def _modif(self, method):
        #send the request
        # response_put = self._send_request(parser, data)
        # print(f"{method} :  {response_put}")
        # dependencies.set_equivalence_method_codes(response_put.status_code,  response_put.body,method)
        # print("PUT Code: ", dependencies.equivalence_put_codes)
        # verify if the status_code are similar
        r = dependencies.compare_status_codes(dependencies.equivalence_post_codes,method)
        
        if(method == "PUT" and len(dependencies.equivalence_put_codes)>0) :
            print(f"POST -> PUT   MR Equivalence : OK \n++++++++++++++" if len(r) == 0 else r)

        if(method == "DELETE" and len(dependencies.equivalence_delete_codes)>0) :
            print(f"POST -> DELETE   MR Equivalence : OK" if len(r) == 0 else r)
        

    def _render_last_request(self, seq):
        """ Render the last request of the sequence and inspect the status
        code of the response. If it's any of 20x, we have probably hit a bug.

        @param seq: The sequence whose last request we will try to render.
        @type  seq: Sequence Class object.

        @return: None
        @rtype : None

        """
        # print("2- We're In _render_last_request\n")
        request = seq.last_request
        for rendered_data, parser,_,updated_writer_variables, replay_blocks in\
            request.render_iter(self._req_collection.candidate_values_pool,
                                skip=request._current_combination_id):
            # Hold the lock (because other workers may be rendering the same
            # request) and check whether the current rendering is known from the
            # past to lead to invalid status codes. If so, skip the current
            # rendering.
            if self._lock is not None:
                self._lock.acquire()
            should_skip = Monitor().is_invalid_rendering(request)
            if self._lock is not None:
                self._lock.release()

            # Skip the loop and don't forget to increase the counter.
            if should_skip:
                RAW_LOGGING("Skipping rendering: {}".\
                            format(request._current_combination_id))
                request._current_combination_id += 1
                continue

            rendered_data = seq.resolve_dependencies(rendered_data)

            endpoint = rendered_data.strip().split('\n')[0].strip().rsplit(" ", 1)[0]

            # print("rendered data : \n", rendered_data)
            response = self._send_request(parser, rendered_data)

            rendering_is_valid = response.has_valid_code()
            if rendering_is_valid:
                for name,v in updated_writer_variables.items():
                    dependencies.set_variable(name, v)
            # print("3- We're In _render_last_request\n")
             #store the reponse status code of post_request somewhere    
            m = [(s.method , endpoint ) for s in seq ]
            print(f"{'>'*15}\n Request - Endpoint =\n{m}\n{'>'*15}\n  ")    
            if seq.last_request.method.startswith('POST') and response.has_valid_code() :

                body = json.loads(response.body)
                dependencies.set_equivalence_method_codes(response.status_code,  response.body)


            if seq.last_request.method.startswith('PUT') and response.has_valid_code() :

                dependencies.set_equivalence_method_codes(response.status_code,  response.body, "PUT")

            
            if seq.last_request.method.startswith('DELETE') and response.has_valid_code() :

                dependencies.set_equivalence_method_codes(response.status_code,  response.body, "DELETE")
    
            # Append the rendered data to the sent list as we will not be rendering
            # with the sequence's render function
            seq.append_data_to_sent_list(request.method_endpoint_hex_definition,
                                         rendered_data, parser, response, replay_blocks=replay_blocks)
            if response and  self._rule_violation(seq, response):
                print("="*10,"\n resp and rule violation \n , Method -> ",self._sequence.last_request.method)
                self._print_suspect_sequence(seq, response)
                print(seq, dependencies.equivalence_post_codes)

                self._modif( "PUT")

                self._modif( "DELETE")

                # if seq.last_request.method.startswith('POST') and response.has_valid_code() :
                #     ###################################################################
                #     #modify the rendered_data and send a put request:
                #     put_data = self._render_data_modif_post_put(rendered_data, response.body,'PUT')
                #     self._modif(put_data, parser,body, "PUT")
                   
                #     ###################################################################
                #     #modify the Post rendered_data and send a Delete request:
                #     del_data = self._render_data_modif_post_put(rendered_data, response.body,'DELETE')
                #     self._modif(del_data, parser, body, "DELETE")

                BugBuckets.Instance().update_bug_buckets(seq, response.status_code, origin=self.__class__.__name__)
            # else : 
            #     print("\n------ Violation Found -----------\n")
            #     print(f"{response.status_code} \t {self._rule_violation(seq, response)} \t {seq.last_request.method}")
            #     print(f"\n{'-'*15}\n")
        
   
    def _get_authentication_method(self):
        """ Trys to find out the authentication method used (if any).

        @return: The authenctication methid used.
        @rtype : Str

        """
        try:
            token1 = self._custom_mutations[primitives.CUSTOM_PAYLOAD][STATIC_OAUTH_TOKEN]
            return STATIC_OAUTH_TOKEN
        except Exception:
            pass

        from engine.core.request_utilities import latest_token_value as token1
        if token1 is not NO_TOKEN_SPECIFIED:
            return primitives.REFRESHABLE_AUTHENTICATION_TOKEN

        return STATIC_OAUTH_TOKEN

 
