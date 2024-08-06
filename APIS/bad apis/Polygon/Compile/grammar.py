""" THIS IS AN AUTOMATICALLY GENERATED FILE!"""
from __future__ import print_function
import json
from engine import primitives
from engine.core import requests
from engine.errors import ResponseParsingException
from engine import dependencies
req_collection = requests.RequestCollection([])
# Endpoint: /v1/companies, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("companies"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("sort="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("perpage="),
    primitives.restler_fuzzable_number("1.23"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_number("1.23"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("apiKey="),
    primitives.restler_fuzzable_string("HdKneHQE7oUcTVAy4jbD3BVdlLPsfEIb", quoted=False, examples = ["HdKneHQE7oUcTVAy4jbD3BVdlLPsfEIb"] ),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.polygon.io\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v1/companies"
)
req_collection.add_request(request)

# Endpoint: /v1/currencies, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("currencies"),
     primitives.restler_static_string("?"),
    primitives.restler_static_string("apiKey="),
    primitives.restler_fuzzable_string("HdKneHQE7oUcTVAy4jbD3BVdlLPsfEIb", quoted=False, examples = ["HdKneHQE7oUcTVAy4jbD3BVdlLPsfEIb"] ),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.polygon.io\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v1/currencies"
)
req_collection.add_request(request)

# Endpoint: /v1/historic/agg/{size}/{symbol}/{date}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("historic"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("agg"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("size", ['second','minute']  ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_date("2019-06-26", quoted=False),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("offset="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("limit="),
    primitives.restler_fuzzable_int("1"),
     primitives.restler_static_string("?"),
    primitives.restler_static_string("apiKey="),
    primitives.restler_fuzzable_string("HdKneHQE7oUcTVAy4jbD3BVdlLPsfEIb", quoted=False, examples = ["HdKneHQE7oUcTVAy4jbD3BVdlLPsfEIb"] ),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.polygon.io\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v1/historic/agg/{size}/{symbol}/{date}"
)
req_collection.add_request(request)

# Endpoint: /v1/historic/forex/{from}/{to}/{date}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("historic"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("forex"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_date("2019-06-26", quoted=False),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("offset="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("limit="),
    primitives.restler_fuzzable_int("1"),
     primitives.restler_static_string("?"),
    primitives.restler_static_string("apiKey="),
    primitives.restler_fuzzable_string("HdKneHQE7oUcTVAy4jbD3BVdlLPsfEIb", quoted=False, examples = ["HdKneHQE7oUcTVAy4jbD3BVdlLPsfEIb"] ),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.polygon.io\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v1/historic/forex/{from}/{to}/{date}"
)
req_collection.add_request(request)

# Endpoint: /v1/historic/quotes/{symbol}/{date}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("historic"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("quotes"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_date("2019-06-26", quoted=False),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("offset="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("limit="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("apiKey="),
    primitives.restler_fuzzable_string("HdKneHQE7oUcTVAy4jbD3BVdlLPsfEIb", quoted=False, examples = ["HdKneHQE7oUcTVAy4jbD3BVdlLPsfEIb"] ),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.polygon.io\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v1/historic/quotes/{symbol}/{date}"
)
req_collection.add_request(request)

# Endpoint: /v1/historic/trades/{symbol}/{date}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("historic"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("trades"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_date("2019-06-26", quoted=False),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("offset="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("limit="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("apiKey="),
    primitives.restler_fuzzable_string("HdKneHQE7oUcTVAy4jbD3BVdlLPsfEIb", quoted=False, examples = ["HdKneHQE7oUcTVAy4jbD3BVdlLPsfEIb"] ),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.polygon.io\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v1/historic/trades/{symbol}/{date}"
)
req_collection.add_request(request)

# Endpoint: /v1/last/currencies/{from}/{to}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("last"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("currencies"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
     primitives.restler_static_string("?"),
    primitives.restler_static_string("apiKey="),
    primitives.restler_fuzzable_string("HdKneHQE7oUcTVAy4jbD3BVdlLPsfEIb", quoted=False, examples = ["HdKneHQE7oUcTVAy4jbD3BVdlLPsfEIb"] ),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.polygon.io\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v1/last/currencies/{from}/{to}"
)
req_collection.add_request(request)

# Endpoint: /v1/last/stocks/{symbol}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("last"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("stocks"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
     primitives.restler_static_string("?"),
    primitives.restler_static_string("apiKey="),
    primitives.restler_fuzzable_string("HdKneHQE7oUcTVAy4jbD3BVdlLPsfEIb", quoted=False, examples = ["HdKneHQE7oUcTVAy4jbD3BVdlLPsfEIb"] ),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.polygon.io\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v1/last/stocks/{symbol}"
)
req_collection.add_request(request)

# Endpoint: /v1/last_quote/currencies/{from}/{to}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("last_quote"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("currencies"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
     primitives.restler_static_string("?"),
    primitives.restler_static_string("apiKey="),
    primitives.restler_fuzzable_string("HdKneHQE7oUcTVAy4jbD3BVdlLPsfEIb", quoted=False, examples = ["HdKneHQE7oUcTVAy4jbD3BVdlLPsfEIb"] ),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.polygon.io\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v1/last_quote/currencies/{from}/{to}"
)
req_collection.add_request(request)

# Endpoint: /v1/last_quote/stocks/{symbol}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("last_quote"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("stocks"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
     primitives.restler_static_string("?"),
    primitives.restler_static_string("apiKey="),
    primitives.restler_fuzzable_string("HdKneHQE7oUcTVAy4jbD3BVdlLPsfEIb", quoted=False, examples = ["HdKneHQE7oUcTVAy4jbD3BVdlLPsfEIb"] ),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.polygon.io\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v1/last_quote/stocks/{symbol}"
)
req_collection.add_request(request)
