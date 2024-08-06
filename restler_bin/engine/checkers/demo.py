import requests 
import json

    
def checker_update_equivalence(id, endpoint, response,base_url):
        """ Update the checker with the id of the item1 in the response
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
                
        print("checker_update_equivalence\n\n")
        print(f"1- Execution of POST Request for item1:\n Request: POST {endpoint} \n Response : {response} \n")

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
        
        print(f"2- Execution of PUT Request for item1:\n Request: PUT {endpoint}/{id} \n data : {data} \n")

        #send the request
        url = f"{base_url}{endpoint}{id}/"
        response1 = requests.put(url, json=data)
        response1 = json.loads(response1.text)
        # response.raise_for_status()

        print(f"Response 1 : {response1} \n")
        

        print(f"\n3- Execution of POST Request for item2:\n Request: POST {endpoint} \n data : {data} \n")
        #send the request
        url = f"{base_url}{endpoint}"
        response2 = requests.post(url, json=data)
        response2 = json.loads(response2.text)
        print(f"Response 2 : {response2} \n")
        
        data1 = {key: value for key, value in response1.items() if key != 'id' and key != 'created_at' and key != 'updated_at'}
        data2 = {key: value for key, value in response2.items() if key != 'id' and key != 'created_at' and key != 'updated_at'}
        
        if data1 == data2:
                print("Equivalence OK")
        else:   
                print("Equivalence KO")


base_url = "http://localhost:8000"
endpoint = "/api/products/"
url = f"{base_url}{endpoint}"

data = {"id":195,"name":"fuzzstring","description":"fuzzstring","price":"100.00"}
response = requests.post(url, json=data)
print(f"Response : {response} \n")

id = json.loads(response.text)['id']
# print(f"id : {id} \n")
checker_update_equivalence( id, endpoint, response.text,base_url)