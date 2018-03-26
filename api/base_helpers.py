import time
import json


class BaseHelpers(object):
    """
    Class which contains common helpers for all endpoints
    """

    @staticmethod
    def wait_until_expression_will_be_true(condition, message='', timeout=5, period=0.25, *args, **kwargs):
        must_end = time.time() + timeout
        while time.time() < must_end:
            if condition:
                return True
            time.sleep(period)
        raise Exception("Timeout {} sec + %s".format(timeout) % message)

    @staticmethod
    def check_values_in_response_body(response_content, values_to_check):
        return all([value.encode("utf-8") in response_content for value in values_to_check])

    @staticmethod
    def parse_response_json(response, json_key):
        return json.loads(response.content)[json_key]
