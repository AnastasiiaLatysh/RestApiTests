import time
import json


class BaseHelpers(object):
    """
    Class which contains common helpers for all endpoints
    """
    @staticmethod
    def check_values_in_response_body(response_content, values_to_check):
        return all([value.encode("utf-8") in response_content for value in values_to_check])

    @staticmethod
    def parse_response_json(response, json_key):
        return json.loads(response.content)[json_key]
