import requests
import json

# Load the grammar.json content (assuming it's already loaded into a variable named grammar_data)
# grammar_data = json.loads(YOUR_GRAMMAR_JSON_CONTENT)

# # Base URL for the API
# BASE_URL = "https://api.thecatapi.com/v1"







def get_grammar_data(file_path):
    """
    Extract the base URL from the RESTler grammar.json file.
    """
    with open(file_path, 'r') as file:
        grammar = json.load(file)
    
    return grammar

def get_base_url_from_grammar(grammar):  
    url = grammar['Requests'][0]["headers"][1][1]
    if url:
        return   url 
    else:
        return  "Base URL not found" 


# File path
file_path = 'Compile/grammar.json'

# Load the grammar.json content (assuming it's already loaded into a variable named grammar_data)
grammar_data = get_grammar_data(file_path)

# Base URL for the API
BASE_URL = get_base_url_from_grammar(grammar_data)
print(BASE_URL)


# Function to construct and send HTTP requests
def send_request(method, endpoint, headers, params={}, data=None):
    url = f"{BASE_URL}{endpoint}"
    # Ensure the URL starts with http:// or https://
    if not url.startswith(('http://', 'https://')):
        url = 'http://' + url  # Default to HTTP if no scheme is specified

    response = requests.request(method, url, headers=headers, params=params, json=data)
    print(f"URL: {url}")
    print(f"Method: {method}")
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.json()}\n ------------ \n")

# Iterate over the requests defined in the grammar
for request in grammar_data['Requests']:
    method = request['method']
    endpoint = ''.join([part['Constant'][1] for part in request['path'] if 'Constant' in part])
    headers = {param[0]: param[1] for param in request['headers']}
    params = {}
    body = {}

    # Handling query parameters
    if 'queryParameters' in request and request['queryParameters']:
        for param_group in request['queryParameters']:
            for param in param_group[1]['ParameterList']:
                params[param['name']] = param['payload']['LeafNode']['payload']['Fuzzable']['exampleValue']

    # Handling body parameters
    if 'bodyParameters' in request and request['bodyParameters']:
        for p in request["bodyParameters"][0][1]['ParameterList']:
            for q in p['payload']["InternalNode"][1] : 
               body[q['LeafNode']['name']] = q['LeafNode']['payload']['Fuzzable']['exampleValue']

        # body = {p['name']: json.loads(p['payload']["InternalNode"][1]['LeafNode']['payload']['Fuzzable']['exampleValue'])
        #         for p in request['bodyParameters'][0][1]['ParameterList']}
    
    send_request(method, endpoint, headers, params, body)


# import threading
# import requests
# import time

# # Fonction pour envoyer une requête GET et mesurer le temps de réponse
# def send_request(url):
#     start_time = time.time()
#     response = requests.get(url)
#     response_time = time.time() - start_time
#     print(f"Thread {threading.current_thread().name}: Response Time = {response_time:.2f}s")

# # L'URL cible pour la requête GET
# url = "http://api.example.com/articles/123"

# # Nombre de threads à lancer simultanément pour simuler les utilisateurs simultanés
# num_threads = 50

# # Créer et démarrer les threads
# threads = []
# for i in range(num_threads):
#     thread = threading.Thread(target=send_request, args=(url,), name=f"Thread-{i+1}")
#     threads.append(thread)
#     thread.start()

# # Attendre que tous les threads aient terminé
# for thread in threads:
#     thread.join()

# print("All requests have been completed.")
