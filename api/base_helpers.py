import json


def check_values_in_response_body(response_content, values_to_check):
    return all([value.encode("utf-8") in response_content for value in values_to_check])


def parse_response_json(response, json_key):
    return json.loads(response.content)[json_key]
