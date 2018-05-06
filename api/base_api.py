import json
import requests
from configs.config import Config
from lib.logger import  logger


class BaseApi(object):
    """
    Class which represents common api methods for any endpoint
    """

    BASE_URL = Config.base_url
    API_VERSION = Config.api_version

    def __init__(self, default_headers=''):
        if default_headers:
            self.default_headers = default_headers
        else:
            self.default_headers = {"Content-Type": "application/json"}

    @logger("GET")
    def get(self, base_url, endpoint, **kwargs):
        """
        Method which executes GET request on specified endpoint
        :param base_url: url to which request should be sent
        :param endpoint: endpoint to which request should be sent
        :param \*\*kwargs: Optional arguments that ``request`` takes
        :return: requests.Response object
        """
        response = requests.get(base_url + endpoint, headers=kwargs["headers"])
        return response

    @logger("POST")
    def post(self, base_url, endpoint, data, **kwargs):
        """
        Method which executes POST request on specified endpoint
        :param base_url: url to which request should be sent
        :param endpoint: endpoint to which request should be sent
        :param data: (dict) which should be sent in request body to create new contact
        :param \*\*kwargs: Optional arguments that ``request`` takes.
        :return: requests.Response object
        """
        response = requests.post(base_url + endpoint, data=json.dumps(data), headers=self.default_headers)
        return response

    @logger("DELETE")
    def delete(self, base_url, endpoint, **kwargs):
        """
        Method which executes DELETE request on specified endpoint
        :param base_url: url to which request should be sent
        :param endpoint: endpoint to which request should be sent
        :param \*\*kwargs: Optional arguments that ``request`` takes.
        :return: requests.Response object
        """
        response = requests.delete(base_url + endpoint)
        return response

    @logger("PUT")
    def put(self, base_url, endpoint, data, **kwargs):
        """
        Method which executes PUT request on specified endpoint
        :param base_url: url to which request should be sent
        :param endpoint: endpoint to which request should be sent
        :param data: (dict) which should be sent in request body to update contact info
        :param \*\*kwargs: Optional arguments that ``request`` takes.
        :return: requests.Response object
        """
        response = requests.put(base_url + endpoint, data=json.dumps(data), headers=self.default_headers)
        return response

    @logger("PATCH")
    def patch(self, base_url, endpoint, data, **kwargs):
        """
        Method which executes PATCH request on specified endpoint
        :param base_url: url to which request should be sent
        :param endpoint: endpoint to which request should be sent
        :param data: (dict) which should be sent in request body to partial update of contact's info
        :param \*\*kwargs: Optional arguments that ``request`` takes.
        :return: requests.Response object
        """
        response = requests.patch(base_url + endpoint, data=json.dumps(data), headers=self.default_headers)
        return response
