""" THIS IS AN AUTOMATICALLY GENERATED FILE!"""
from __future__ import print_function
import json
from engine import primitives
from engine.core import requests
from engine.errors import ResponseParsingException
from engine import dependencies
req_collection = requests.RequestCollection([])
# Endpoint: /images/search, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("images"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("search"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("size="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["med"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("mime_types="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["jpg"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("format="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["json"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("has_breeds="),
    primitives.restler_fuzzable_bool("true", examples=["true"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("order="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["RANDOM"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1", examples=["0"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("limit="),
    primitives.restler_fuzzable_int("1", examples=["1"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.thecatapi.com\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["application/json"]),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("x-api-key: "),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["live_bGSVuf7sQpH25ed73ahSkLItqu14rVG5ZGrY4W8LBM66bhEFkokhc1pWBoCJvLpe"]),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/images/search"
)
req_collection.add_request(request)

# Endpoint: /images/BkIEhN3pG, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("images"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("BkIEhN3pG"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.thecatapi.com\r\n"),
    primitives.restler_static_string("x-api-key: "),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["live_bGSVuf7sQpH25ed73ahSkLItqu14rVG5ZGrY4W8LBM66bhEFkokhc1pWBoCJvLpe"]),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/images/BkIEhN3pG"
)
req_collection.add_request(request)

# Endpoint: /images, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("images"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("limit="),
    primitives.restler_fuzzable_int("1", examples=["10"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1", examples=["0"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("order="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["DESC"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.thecatapi.com\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["application/json"]),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("x-api-key: "),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["live_bGSVuf7sQpH25ed73ahSkLItqu14rVG5ZGrY4W8LBM66bhEFkokhc1pWBoCJvLpe"]),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/images"
)
req_collection.add_request(request)

# Endpoint: /images/upload, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("images"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("upload"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.thecatapi.com\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["multipart/form-data"]),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("x-api-key: "),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["live_bGSVuf7sQpH25ed73ahSkLItqu14rVG5ZGrY4W8LBM66bhEFkokhc1pWBoCJvLpe"]),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/images/upload"
)
req_collection.add_request(request)

# Endpoint: /images/{image_id}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("images"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["dMsUj1-nz"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.thecatapi.com\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["application/json"]),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("x-api-key: "),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["live_bGSVuf7sQpH25ed73ahSkLItqu14rVG5ZGrY4W8LBM66bhEFkokhc1pWBoCJvLpe"]),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/images/{image_id}"
)
req_collection.add_request(request)

# Endpoint: /images/{image_id}/breeds, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("images"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("breeds"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.thecatapi.com\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["application/json"]),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/images/{image_id}/breeds"
)
req_collection.add_request(request)

# Endpoint: /images/{image_id}/breeds, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("images"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("breeds"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.thecatapi.com\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["application/json"]),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("x-api-key: "),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["live_bGSVuf7sQpH25ed73ahSkLItqu14rVG5ZGrY4W8LBM66bhEFkokhc1pWBoCJvLpe"]),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_fuzzable_object("{ \"fuzz\": false }", examples=["{\"breed_id\":\"10\"}"]),
    primitives.restler_static_string("\r\n"),

],
requestId="/images/{image_id}/breeds"
)
req_collection.add_request(request)

# Endpoint: /images/{image_id}/breeds/{breed_id}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("images"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("breeds"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.thecatapi.com\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["application/json"]),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("x-api-key: "),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["live_bGSVuf7sQpH25ed73ahSkLItqu14rVG5ZGrY4W8LBM66bhEFkokhc1pWBoCJvLpe"]),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/images/{image_id}/breeds/{breed_id}"
)
req_collection.add_request(request)

# Endpoint: /breeds, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("breeds"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("limit="),
    primitives.restler_fuzzable_int("1", examples=["10"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1", examples=["0"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.thecatapi.com\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["application/json"]),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/breeds"
)
req_collection.add_request(request)

# Endpoint: /breeds/{breed_id}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("breeds"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.thecatapi.com\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["application/json"]),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/breeds/{breed_id}"
)
req_collection.add_request(request)

# Endpoint: /breeds/{breed_id}/facts, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("breeds"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["ragd"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("facts"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("limit="),
    primitives.restler_fuzzable_int("1", examples=["5"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1", examples=["0"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("order="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["ASC"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.thecatapi.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/breeds/{breed_id}/facts"
)
req_collection.add_request(request)

# Endpoint: /breeds/search, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("breeds"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("search"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("q="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["air"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("attach_image="),
    primitives.restler_fuzzable_int("1", examples=["1"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.thecatapi.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/breeds/search"
)
req_collection.add_request(request)

# Endpoint: /favourites, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("favourites"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.thecatapi.com\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["application/json"]),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("x-api-key: "),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["live_bGSVuf7sQpH25ed73ahSkLItqu14rVG5ZGrY4W8LBM66bhEFkokhc1pWBoCJvLpe"]),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/favourites"
)
req_collection.add_request(request)

# Endpoint: /favourites, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("favourites"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.thecatapi.com\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["application/json"]),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("x-api-key: "),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["live_bGSVuf7sQpH25ed73ahSkLItqu14rVG5ZGrY4W8LBM66bhEFkokhc1pWBoCJvLpe"]),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_fuzzable_object("{ \"fuzz\": false }", examples=["""{\n\t\"image_id\":asf2,\n\t\"sub_id\": \"my-user-1234\"\n}"""]),
    primitives.restler_static_string("\r\n"),

],
requestId="/favourites"
)
req_collection.add_request(request)

# Endpoint: /favourites/{favourite_id}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("favourites"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.thecatapi.com\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["application/json"]),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("x-api-key: "),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["live_bGSVuf7sQpH25ed73ahSkLItqu14rVG5ZGrY4W8LBM66bhEFkokhc1pWBoCJvLpe"]),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/favourites/{favourite_id}"
)
req_collection.add_request(request)

# Endpoint: /favourites/{favourite_id}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("favourites"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.thecatapi.com\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["application/json"]),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("x-api-key: "),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["live_bGSVuf7sQpH25ed73ahSkLItqu14rVG5ZGrY4W8LBM66bhEFkokhc1pWBoCJvLpe"]),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/favourites/{favourite_id}"
)
req_collection.add_request(request)

# Endpoint: /votes, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("votes"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.thecatapi.com\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["application/json"]),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("x-api-key: "),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["live_bGSVuf7sQpH25ed73ahSkLItqu14rVG5ZGrY4W8LBM66bhEFkokhc1pWBoCJvLpe"]),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/votes"
)
req_collection.add_request(request)

# Endpoint: /votes, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("votes"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.thecatapi.com\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["application/json"]),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("x-api-key: "),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["live_bGSVuf7sQpH25ed73ahSkLItqu14rVG5ZGrY4W8LBM66bhEFkokhc1pWBoCJvLpe"]),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_fuzzable_object("{ \"fuzz\": false }", examples=["{\"image_id\":\"asf2\",\"sub_id\":\"my-user-1234\",\"value\":\"1\"}"]),
    primitives.restler_static_string("\r\n"),

],
requestId="/votes"
)
req_collection.add_request(request)

# Endpoint: /votes/{vote_id}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("votes"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.thecatapi.com\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["application/json"]),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("x-api-key: "),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["live_bGSVuf7sQpH25ed73ahSkLItqu14rVG5ZGrY4W8LBM66bhEFkokhc1pWBoCJvLpe"]),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/votes/{vote_id}"
)
req_collection.add_request(request)

# Endpoint: /vote/{vote_id}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("vote"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.thecatapi.com\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["application/json"]),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("x-api-key: "),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["live_bGSVuf7sQpH25ed73ahSkLItqu14rVG5ZGrY4W8LBM66bhEFkokhc1pWBoCJvLpe"]),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/vote/{vote_id}"
)
req_collection.add_request(request)

# Endpoint: /webhooks, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("webhooks"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.thecatapi.com\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_fuzzable_object("{ \"fuzz\": false }", examples=["{\"name\":\"Charef\",\"url\":\"https://webhook.site/8ff\",\"events\":[\"favourite.created\"]}"]),
    primitives.restler_static_string("\r\n"),

],
requestId="/webhooks"
)
req_collection.add_request(request)

# Endpoint: /facts, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("facts"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.thecatapi.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/facts"
)
req_collection.add_request(request)
