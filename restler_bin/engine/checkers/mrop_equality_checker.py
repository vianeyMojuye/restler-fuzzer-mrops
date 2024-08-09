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

import requests 


STATIC_OAUTH_TOKEN = 'static_oauth_token'




class MropEqualityChecker(CheckerBase):
    """ Checker For EqualityDisjointMROP Operation """

    
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
        self._equivalence_post_codes = []
        self._custom_mutations = self._req_collection.candidate_values_pool.candidate_values

        # print("\n ********** self._custom_mutations :***********: \t",  self._custom_mutations)
        # self._authentication_method = self._get_authentication_method()
        # print("\n **********auth***********: \t", self._authentication_method)
        # if self._authentication_method not\
        #     in [STATIC_OAUTH_TOKEN, primitives.REFRESHABLE_AUTHENTICATION_TOKEN]:
        #     print("\n **********nothing*********** \n")
        #     return
        
        self._render_last_request(self._sequence)

    
    # def _render_data_modif_post_get(self, s, resp_body):
    #     """
    #         modif the post rendered_data into a get request
    #         @param resp_body : the POST response body
    #         @param resp_body : str

    #         @return :
    #            s_modified : the modified  (Delete) rendered_data
    #            s_modified : str
    #     """

    #     # Parsing the response body to extract the new 'id' and 'checksum' values
    #     resp_data = json.loads(resp_body)
    #     new_id = resp_data["id"]

    #     # Replace the POST method with GET and update the URI with the new 'id'

    #     s_modified = s.replace("POST /api/blog/posts", f"GET /api/blog/posts/{new_id}", 1)

    #     # Replace the original 'id' value with the new 'id' in the JSON body
    #     # Since 'id' is a unique identifier, its value should be replaced only in the JSON body, not in the URI again
    #     import re
    #     s_modified = re.sub(r'\{[^}]*\}', f'', s_modified)

    #     return s_modified



    def checker_equality(self, id, endpoint, response,base_url):
        """ Update equality checker with the id of the item1 in the response
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
                
        mystring =  f"{'>'*50}\n{'_'*50}\nchecker_Equality Operations PUT item1  vs PUT item1 \n\n"      
        print(f"{'>'*15}\nchecker_Equality Operations PUT item1  vs PUT item1  \n\n")
        mystring+= f"1- Execution of PUT Request for item1:\n Request: PUT  {endpoint}{id}/ \n Response : {response} \n"
        print(f"1- Execution of PUT Request for item1:\n Request: PUT {endpoint}{id}/ \n Response : {response} \n")

        
        endpoint = endpoint.strip().split(' ')[-1].strip()
        
         # Convert JSON string to dictionary
        data = json.loads(response)
       
        mystring+= f"\n2- Execution of PUT Request for item1:\n Request: PUT {endpoint}{id}/ \n data : {data} \n"
        print(f"\n2- Execution of PUT Request for item1:\n Request: PUT {endpoint}{id}/ \n data : {data} \n" )
        #send the request
        url = f"{base_url}{endpoint}{id}/"
        response2 = requests.put(url, json=data)
        response2 = json.loads(response2.text)
        response = json.loads(response)

        mystring+= f"Response PUT Item 1 : {response2} \n"
        print(f"Response PUT Item 1 : {response2} \n")
        
        try :

            data1 = {key: value for key, value in response.items() if  key != 'created_at' and key != 'updated_at'}
            data2 = {key: value for key, value in response2.items() if  key != 'created_at' and key != 'updated_at'}
            assert data1 == data2
            mystring+= f" Equality sequences Respected : \n Response PUT item 1  == Response PUT Item 1 \n"
            print(f" Equality sequences Respected : \n Response PUT item 1  == Response PUT Item 1 \n")
        except Exception as e:
            
            found = True
            mystring+= f"{'+'*20}\n Bug where found {'+'*20}\n  Equality relations not Respected Error in PUT item : \n Response PUT item 1  != Response PUT Item 1 \n"
            print(f"{'+'*20}\n Bug where found {'+'*20}\n  Equality relations not Respected Error in PUT item : \n Response PUT item 1  != Response PUT Item 1 \n")
        if found :
            write_file("checker_equality.txt", mystring)
       

    def checker_del_equality(self, id, endpoint, response,base_url):
        """ Delete equality checker with the id of the item1 in the response
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
        
       
                
        def write_file(filename, text):
                with open(filename, 'a') as f:
                    f.write(text)

        found = False
                
        endpoint = endpoint.strip().split(' ')[-1].strip()

        mystring =  f"{'>'*50}\n{'_'*50}\nchecker_Equality Operations DELETE item1  vs DELETE item2 \n\n"      
        print(f"{'>'*15}\nchecker_Equality Operations DELETE item1  vs DELETE item2  \n\n")
        mystring+= f"1- Execution of DELETE Request for item1:\n Request: DELETE  {endpoint}{id}/ \n "
        print(f"1- Execution of DELETE Request for item1:\n Request: DELETE {endpoint}{id}/ \n")

        #delete the item1
        url = f"{base_url}{endpoint}{id}/"
        response = requests.delete(url)
    
        


        mystring+= f"Response (STATUS CODE) DELETE Item 1 : {response.status_code} \n"
        print(f"Response DELETE Item 1 : {response.status_code} \n")
       
        mystring+= f"\n2- Execution of DELETE Request for item2:\n Request: DELETE {endpoint}{int(id)-1}/ \n "
        print(f"\n2- Execution of DELETE Request for item2:\n Request: DELETE {endpoint}{int(id)-1}/ \n" )
        #send the request
        url = f"{base_url}{endpoint}{int(id)-1}/"
        response2 = requests.delete(url)
      

        mystring+= f"Response DELETE Item 2 : {response2.status_code} \n"
        print(f"Response DELETE Item 2 : {response2.status_code} \n")

        #get request for item1
        mystring+= f"\n3- Execution of GET Request for item1:\n Request: GET {endpoint}{id}/ \n "
        print(f"\n3- Execution of GET Request for item1:\n Request: GET {endpoint}{id}/ \n" )
        url = f"{base_url}{endpoint}{id}/"
        response3 = requests.get(url)
        response3 = {"status_code": response3.status_code, "body": json.loads(response3.text)}

        mystring+= f"Response GET Item 1 : {response3} \n"
        print(f"Response GET Item 1 : {response3} \n")

        #get request for item2
        mystring+= f"\n4- Execution of GET Request for item2:\n Request: GET {endpoint}{int(id)-1}/ \n "
        print(f"\n4- Execution of GET Request for item2:\n Request: GET {endpoint}{int(id)-1}/ \n" )
        url = f"{base_url}{endpoint}{int(id)-1}/"
        response4 = requests.get(url)
        response4 = {"status_code": response4.status_code, "body": json.loads(response4.text)}

        mystring+= f"Response GET Item 2 : {response4} \n"
        print(f"Response GET Item 2 : {response4} \n")
        
        
        try :

            assert response3['status_code'] == response4['status_code'] == 404
            mystring+= f" Equality sequences Respected : \n(After Deletion of Item1 and Item2) Response PUT item 1  == Response PUT Item 1 \n"
            print(f" Equality sequences Respected : \n(After Deletion of Item1 and Item2) Response PUT item 1  == Response PUT Item 1 \n")
        except Exception as e:
            
            found = True
            mystring+= f"{'+'*20}\n Bug where found {'+'*20}\n  Equality relations not Respected Error in DELETE item : \n (After Deletion of Item1 and Item2) Response GET item 1  != Response GET Item 1 \n"
            print(f"{'+'*20}\n Bug where found {'+'*20}\n  Equality relations not Respected Error in DELETE item : \n (After Deletion of Item1 and Item2) Response GET item 1  != Response GET Item 1 \n")
        if found :
            write_file("checker_del_equality.txt", mystring)
       

      



    def _modif(self, method):
        """
            sends the follow-up request(modifciation of post request) and verify if the metamorphic relationship was respected
            @param data : request to be sent
            @param data : str
            @param body : json representation of Post Resquest response body
            @param body: json
            @param method : method applied on the request (ex: PUT?GET, etc..)
            @param body: str

        
        """
        
        # response_modif = self._send_request(parser, data)
        # print(f"{method} :  {response_put}")
        # dependencies.set_equivalence_post_codes(response_modif.status_code,  response_modif.body, body['id'],method)
        # # print("PUT Code: ", dependencies.equivalence_put_codes)
        # # verify if the status_code are similar
        # r = dependencies.compare_for_equality_mrop(dependencies.equivalence_post_codes,dependencies.equivalence_get_codes,method)
        
        # print("POST->POST   MR Equality : OK" if len(r[0]) == 0 else r[0])
        # print(f"POST -> {method}   MR Equality : OK" if len(r[1]) == 0 else r[1])

        r = dependencies.compare_for_equality_mrop(dependencies.equivalence_post_codes,dependencies.equivalence_get_codes,method)
        
        if len(dependencies.equivalence_post_codes)>= 2 :
            print("POST->POST   MR Equality : OK" if len(r[0]) == 0 else r[0])
        if len(dependencies.equivalence_get_codes)>= 1 :
            print(f"POST -> {method}   MR Equality : OK" if len(r[1]) == 0 else r[1])
        

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


            endpoint = rendered_data.strip().split('\n')[0].strip().rsplit(" ", 1)[0]
            rendered_data = seq.resolve_dependencies(rendered_data)
            # print("rendered data : \n", rendered_data)
            response = self._send_request(parser, rendered_data)

            rendering_is_valid = response.has_valid_code()
            if rendering_is_valid:
                for name,v in updated_writer_variables.items():
                    dependencies.set_variable(name, v)
            # print("3- We're In _render_last_request\n")
             #store the reponse status code of post_request somewhere
            m = [(s.method , s.endpoint ) for s in seq ]
            print(f"{'>'*15}\n Request - Endpoint =\n{m}\n{'>'*15}\n  ")      
            if (seq.last_request.method.startswith('PUT') or seq.last_request.method.startswith('POST') ) and response.has_valid_code() :


                if seq.last_request.method.startswith('PUT') :
                    #get the id of the item1  in the response
                    id1 = response.body.split('id":')[1].split(',')[0].split('"')[0]
                    print(f"{'>'*15}\nid1 = {id1}")
                    #get the base url of the api
                    with open('../base_url.txt', 'r') as f:
                        base_url = f.read()
                    print(f"{'>'*15}\nbase_url = {base_url}")
                    print(f"{'>'*15}\nresponse.body = {response.body}")

                    endpoint = endpoint.split('_READER_DELIM_')[0].replace("PUT ", "")
                    #call the checker_equality function
                    self.checker_equality(id1, endpoint, response.body, base_url)
                else :
                     #get the id of the item1  in the response
                    id1 = response.body.split('id":')[1].split(',')[0].split('"')[0]
                    #get the base url of the api
                    with open('../base_url.txt', 'r') as f:
                        base_url = f.read()
                    # print(f"{'>'*15}\nbase_url = {base_url}")
                    # print(f"{'>'*15}\nresponse.body = {response.body}")
                    #call the checker_del_equality function
                    self.checker_del_equality(id1, endpoint, response.body, base_url)
                



                dependencies.set_equivalence_method_codes(response.status_code,  response.body)


          
            # Append the rendered data to the sent list as we will not be rendering
            # with the sequence's render function
            seq.append_data_to_sent_list(request.method_endpoint_hex_definition,
                                         rendered_data, parser, response, replay_blocks=replay_blocks)
            if response and self._rule_violation(seq, response):
                print("resp and rule, Method -> ",self._sequence.last_request.method)
                self._print_suspect_sequence(seq, response)
                print(seq, dependencies.equivalence_post_codes)

                self._modif( "GET")

            #     if seq.last_request.method.startswith('POST') and response.has_valid_code() :
            #         ###################################################################
            #         ###################################################################
            #         #modify the Post rendered_data and send a Get request:
            #         get_data = self._render_data_modif_post_get(rendered_data,response.body)
            #         # print("get_data : ", get_data)
            #         self._modif(get_data, parser, body, "GET")

            BugBuckets.Instance().update_bug_buckets(seq, response.status_code, origin=self.__class__.__name__)

            # print("4-  End : We're In _render_last_request\n")

        
   
