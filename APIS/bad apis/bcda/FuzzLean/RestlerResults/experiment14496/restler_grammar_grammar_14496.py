""" THIS IS AN AUTOMATICALLY GENERATED FILE!"""
from __future__ import print_function
import json
from engine import primitives
from engine.core import requests
from engine.errors import ResponseParsingException
from engine import dependencies
req_collection = requests.RequestCollection([])
# Endpoint: /action/organization_activity_list, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("action"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("organization_activity_list"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("id="),
    primitives.restler_fuzzable_string("ministry-of-agriculture", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: catalogue.data.gov.bc.ca\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/action/organization_activity_list"
)
req_collection.add_request(request)

# Endpoint: /action/organization_activity_list_html, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("action"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("organization_activity_list_html"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("id="),
    primitives.restler_fuzzable_string("ministry-of-agriculture", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: catalogue.data.gov.bc.ca\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/action/organization_activity_list_html"
)
req_collection.add_request(request)

# Endpoint: /action/organization_autocomplete, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("action"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("organization_autocomplete"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("q="),
    primitives.restler_fuzzable_string("ministry", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("limit="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: catalogue.data.gov.bc.ca\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/action/organization_autocomplete"
)
req_collection.add_request(request)

# Endpoint: /action/organization_follower_count, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("action"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("organization_follower_count"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("id="),
    primitives.restler_fuzzable_string("ministry-of-agriculture", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: catalogue.data.gov.bc.ca\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/action/organization_follower_count"
)
req_collection.add_request(request)

# Endpoint: /action/organization_follower_list, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("action"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("organization_follower_list"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("id="),
    primitives.restler_fuzzable_string("ministry-of-agriculture", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: catalogue.data.gov.bc.ca\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/action/organization_follower_list"
)
req_collection.add_request(request)

# Endpoint: /action/organization_list, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("action"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("organization_list"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("offset="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("limit="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: catalogue.data.gov.bc.ca\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/action/organization_list"
)
req_collection.add_request(request)

# Endpoint: /action/organization_list_for_user, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("action"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("organization_list_for_user"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("permission="),
    primitives.restler_fuzzable_string("\"edit_group\"", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: catalogue.data.gov.bc.ca\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/action/organization_list_for_user"
)
req_collection.add_request(request)

# Endpoint: /action/organization_revision_list, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("action"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("organization_revision_list"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("id="),
    primitives.restler_fuzzable_string("ministry-of-agriculture", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: catalogue.data.gov.bc.ca\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/action/organization_revision_list"
)
req_collection.add_request(request)

# Endpoint: /action/organization_show, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("action"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("organization_show"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("id="),
    primitives.restler_fuzzable_string("ministry-of-agriculture", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("include_datasets="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: catalogue.data.gov.bc.ca\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/action/organization_show"
)
req_collection.add_request(request)

# Endpoint: /action/package_activity_list, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("action"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("package_activity_list"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("id="),
    primitives.restler_fuzzable_string("ministry-of-agriculture", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("offset="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("limit="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: catalogue.data.gov.bc.ca\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/action/package_activity_list"
)
req_collection.add_request(request)

# Endpoint: /action/package_activity_list_html, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("action"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("package_activity_list_html"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("id="),
    primitives.restler_fuzzable_string("grizzly-bear-population-units", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("offset="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("limit="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: catalogue.data.gov.bc.ca\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/action/package_activity_list_html"
)
req_collection.add_request(request)

# Endpoint: /action/package_autocomplete, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("action"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("package_autocomplete"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("q="),
    primitives.restler_fuzzable_string( "\"Okanagan Lake\"", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("limit="),
    primitives.restler_fuzzable_int("10"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: catalogue.data.gov.bc.ca\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/action/package_autocomplete"
)
req_collection.add_request(request)

# Endpoint: /action/package_list, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("action"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("package_list"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("offset="),
    primitives.restler_fuzzable_int("0"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("limit="),
    primitives.restler_fuzzable_int("100"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: catalogue.data.gov.bc.ca\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/action/package_list"
)
req_collection.add_request(request)

# Endpoint: /action/package_relationships_list, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("action"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("package_relationships_list"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("id="),
    primitives.restler_fuzzable_string("grizzly-bear-population-units", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("id2="),
    primitives.restler_fuzzable_string("important-fossil-areas", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("rel="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: catalogue.data.gov.bc.ca\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/action/package_relationships_list"
)
req_collection.add_request(request)

# Endpoint: /action/package_revision_list, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("action"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("package_revision_list"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("id="),
    primitives.restler_fuzzable_string("grizzly-bear-population-units", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: catalogue.data.gov.bc.ca\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/action/package_revision_list"
)
req_collection.add_request(request)

# Endpoint: /action/package_search, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("action"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("package_search"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("q="),
    primitives.restler_fuzzable_string( "\"Okanagan Lake\"", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: catalogue.data.gov.bc.ca\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/action/package_search"
)
req_collection.add_request(request)

# Endpoint: /action/package_show, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("action"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("package_show"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("id="),
    primitives.restler_fuzzable_string("grizzly-bear-population-units", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: catalogue.data.gov.bc.ca\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/action/package_show"
)
req_collection.add_request(request)

# Endpoint: /action/related_list, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("action"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("related_list"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("id="),
    primitives.restler_fuzzable_string("", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("dataset="),
    primitives.restler_fuzzable_string("", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("type_filter="),
    primitives.restler_fuzzable_string("", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("sort="),
    primitives.restler_fuzzable_string("", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("featured="),
    primitives.restler_fuzzable_string("", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: catalogue.data.gov.bc.ca\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/action/related_list"
)
req_collection.add_request(request)

# Endpoint: /action/resource_search, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("action"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("resource_search"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("query="),
    primitives.restler_fuzzable_string("format:csv", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("fields="),
    primitives.restler_fuzzable_string("", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("order_by="),
    primitives.restler_fuzzable_string("", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("offset="),
    primitives.restler_fuzzable_int("0"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("limit="),
    primitives.restler_fuzzable_int("0"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: catalogue.data.gov.bc.ca\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/action/resource_search"
)
req_collection.add_request(request)

# Endpoint: /action/resource_show, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("action"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("resource_show"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("id="),
    primitives.restler_fuzzable_string("e6c8bb1d-3726-418b-9b7e-1d97a9bbb817", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("include_tracking="),
    primitives.restler_fuzzable_bool("false"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: catalogue.data.gov.bc.ca\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/action/resource_show"
)
req_collection.add_request(request)

# Endpoint: /action/status_show, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("action"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("status_show"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: catalogue.data.gov.bc.ca\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/action/status_show"
)
req_collection.add_request(request)

# Endpoint: /action/tag_list, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("action"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("tag_list"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("offset="),
    primitives.restler_fuzzable_int("0"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("limit="),
    primitives.restler_fuzzable_int("100"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: catalogue.data.gov.bc.ca\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/action/tag_list"
)
req_collection.add_request(request)
