# Copyright (c) Eunice Vianey Mojuye Toukam.

from __future__ import print_function

from checkers.checker_base import *

from checkers.checker_base import *
from engine.bug_bucketing import BugBuckets
from engine.fuzzing_parameters.fuzzing_utils import *

import engine.primitives as primitives
from utils.logger import raw_network_logging as RAW_LOGGING
import json
import requests 
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


    
    def checker_deletion_consistency(self, id, endpoint, response,base_url):
        """ Delete equivalence checker with the id of the item1 in the response
            @param id: id of the item1 in the response
            @type  id: string   
            @param endpoint: endpoint of the item1 in the response
            @type  endpoint: string
            @return: None
            @rtype : None   
            @param response: response of the item1 in the response
            @type  response: string 
            @param base_url: base url of the api
            @type  base_url: string
        """
        found = False
        def write_file(filename, text):
                with open(filename, 'a') as f:
                    f.write(text)
                
        mystring =  f"{'>'*50}\n{'_'*50}\nchecker_delete_equivalence (POST ,DELETE) item1 vs GET item1 \n\n"      
        print(f"{'>'*15}\nchecker_delete_equivalence (POST ,DELETE) item1 vs GET item1  \n\n")
        mystring+= f"1- Execution of POST Request for item1:\n Request:  {endpoint} \n Response : {response} \n"
        print(f"1- Execution of POST Request for item1:\n Request:  {endpoint} \n Response : {response} \n")

        

        endpoint = endpoint.strip().split(' ')[-1].strip()
        
        mystring+= f"2- Execution of DELETE Request for item1:\n Request: DELETE {endpoint}{id}/ \n"
        print(f"2- Execution of DELETE Request for item1:\n Request: DELETE {endpoint}/{id} \n")

        #send the request
        url = f"{base_url}{endpoint}{id}/"
        response1 = requests.delete(url)
        response1 = f"STATUS_CODE: {response1.status_code}, Message : Product deleted"
        # response.raise_for_status()

        mystring+= f"STATUS CODE of Response DELETE item 1 : {response1} \n"
        print(f"STATUS CODE of Response DELETE item 1 : {response1} \n")
        
        mystring+= f"\n3- Execution of GET Request for item1:\n Request: GET {endpoint}  \n"
        print(f"\n3- Execution of GET Request for item1:\n Request: GET {endpoint}  \n")
        #send the request
        url = f"{base_url}{endpoint}{id}/"
        response2 = requests.get(url)
        response2 =   f"STATUS_CODE: {response2.status_code}, BODY : {json.loads(response2.text)}"

        mystring+= f"Response GET Item 1 : {response2} \n"
        print(f"Response GET Item 1 : {response2} \n")
        
        try :
           
            assert response2.status_code == 404
            mystring+= f"Equivalence sequence Respected : \n Status_CODE of Response DELETE item 1  == 2XX and Status_CODE of Response GET Item 1  == 404 \n"
            print(f"Equivalence sequence Respected : \n Response DELETE item 1  == 2XX and Response GET Item 1  == 404 \n")
        except Exception as e:
            
            # print(e)
            found = True
            mystring+= f"{'+'*20}\n Bug where found {'+'*20}\n Equivalence sequence not Respected : \n Status_CODE of Response DELETE item 1  == 2XX and Status_CODE of Response GET Item 1  == 2XX \n It means that the Delete operation hasn't deleted the item1 \n"
            print(f"Equivalence sequence not Respected : \n Status_CODE of Response DELETE item 1  == 2XX and Status_CODE of Response GET Item 1  == 2XX \n It means that the Delete operation hasn't deleted the item1 \n")
        
        if found :
            write_file("checker_deletion_consistency.txt", mystring)
        

        

   

    def checker_update_equivalence(self, id, endpoint, response,base_url):
        """ Update equivalence checker with the id of the item1 in the response
            @param id: id of the item1 in the response
            @type  id: string   
            @param endpoint: endpoint of the item1 in the response
            @type  endpoint: string
            @return: None
            @rtype : None   
            @param response: response of the item1 in the response
            @type  response: string 
            @param base_url: base url of the api
            @type  base_url: string
        """
        # Function to check if a string represents a digit/number
        def is_string_number(value):
                try:
                    float(value)
                    return True
                except ValueError:
                    return False
                
        def write_file(filename, text):
                with open(filename, 'a') as f:
                    f.write(text)

        found = False
                
        mystring =  f"{'>'*50}\n{'_'*50}\nchecker_update_equivalence (POST ,PUT) item1 vs POST item2 \n\n"      
        print(f"{'>'*15}\nchecker_update_equivalence (POST ,PUT) item1 vs POST item2  \n\n")
        mystring+= f"1- Execution of POST Request for item1:\n Request:  {endpoint} \n Response : {response} \n"
        print(f"1- Execution of POST Request for item1:\n Request:  {endpoint} \n Response : {response} \n")

        # JSON string
        json_string = response

        # Convert JSON string to dictionary
        data = json.loads(json_string)

        # Update the dictionary values based on the conditions
        for key, value in data.items():
            
            if isinstance(value, str) and is_string_number(value):
                data[key] = "50"
            else:
                data[key] = "checker_updation_equivalence"

        del data['created_at']
        del data['updated_at']
        # Print the updated dictionary
        # print(data)
        endpoint = endpoint.strip().split(' ')[-1].strip()
        
        mystring+= f"2- Execution of PUT Request for item1:\n Request: PUT {endpoint}{id}/ \n data : {data} \n"
        print(f"2- Execution of PUT Request for item1:\n Request: PUT {endpoint}/{id} \n data : {data} \n")

        #send the request
        url = f"{base_url}{endpoint}{id}/"
        response1 = requests.put(url, json=data)
        response1 = json.loads(response1.text)
        # response.raise_for_status()

        mystring+= f"Response PUT item 1 : {response1} \n"
        print(f"Response PUT item 1 : {response1} \n")
        
        mystring+= f"\n3- Execution of POST Request for item2:\n Request: POST {endpoint} \n data : {data} \n"
        print(f"\n3- Execution of POST Request for item2:\n Request: POST {endpoint} \n data : {data} \n")
        #send the request
        url = f"{base_url}{endpoint}"
        response2 = requests.post(url, json=data)
        response2 = json.loads(response2.text)

        mystring+= f"Response POST Item 2 : {response2} \n"
        print(f"Response POST Item 2 : {response2} \n")
        
        try :
            data1 = {key: value for key, value in response1.items() if key != 'id' and key != 'created_at' and key != 'updated_at'}
            data2 = {key: value for key, value in response2.items() if key != 'id' and key != 'created_at' and key != 'updated_at'}
            assert data1 == data2
            mystring+= f"Equivalence sequence Respected : \n Response PUT item 1  == Response POST Item 2 \n"
            print(f"Equivalence sequence Respected : \n Response PUT item 1  == Response POST Item 2 \n")
        except Exception as e:
            
            found = True
            mystring+= f"{'+'*20}\n Bug where found {'+'*20}\n Equivalence sequence not Respected : \n Response PUT item 1  != Response POST Item 2 \n"
            print(f"Equivalence sequence not Respected : \n Response PUT item 1  != Response POST Item 2 \n")
        
        if found :
            write_file("checker_update_equivalence.txt", mystring)
       

        

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
            #in case of POST Request: 
            #  Operation Sequence 1: POST item1 with some initial data. 
            #                       then PUT item1 with new data equivalent to a different POST operation.
            # Operation Sequence 2: POST item2 with data equivalent to the PUT operation in Sequence 1.
            # Expected Outcome: The state and response for GET requests on item1 and item2 
            #   should reflect equivalent data except for potentially unique identifiers (e.g., IDs).
            if seq.last_request.method.startswith('POST') and response.has_valid_code() :

                # body = json.loads(response.body)

                #get the id of the item1  in the response
                id1 = response.body.split('id":')[1].split(',')[0].split('"')[0]
                print(f"{'>'*15}\nid1 = {id1}")
                #get the base url of the api
                with open('../base_url.txt', 'r') as f:
                    base_url = f.read()
                print(f"{'>'*15}\nbase_url = {base_url}")
                print(f"{'>'*15}\nresponse.body = {response.body}")
                #call the checker_update_equivalence function
                self.checker_update_equivalence(id1, endpoint, response.body, base_url)
                #call the checker_deletion_consistency function
                self.checker_deletion_consistency(id1, endpoint, response.body, base_url)

                dependencies.set_equivalence_method_codes(response.status_code,  response.body)


            # if seq.last_request.method.startswith('PUT') and response.has_valid_code() :

            #     dependencies.set_equivalence_method_codes(response.status_code,  response.body, "PUT")

            
            # if seq.last_request.method.startswith('DELETE') and response.has_valid_code() :

            #     dependencies.set_equivalence_method_codes(response.status_code,  response.body, "DELETE")
    
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

 
