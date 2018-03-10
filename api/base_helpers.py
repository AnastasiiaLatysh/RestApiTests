import time
import json


class BaseHelpers:
    """
    Class which contains common helpers for all endpoints
    """

    @staticmethod
    def wait_until(condition, timeout=2, period=0.25, *args, **kwargs):
        must_end = time.time() + timeout
        while time.time() < must_end:
            if condition:
                return True
            time.sleep(period)
        raise Exception("Timeout {} sec".format(timeout))

    @staticmethod
    def check_values_in_response_body(response_content, values_to_check):
        return all([value.encode("utf-8") in response_content for value in values_to_check])

    @staticmethod
    def parse_response_json(response, json_key):
        return json.loads(response.content)[json_key]
