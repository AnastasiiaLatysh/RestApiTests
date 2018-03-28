import json
import requests
from api.logger import log
from configs.configs import Configs


class BaseApi(object):
    """
    Class which represents common api methods for any endpoint
    """

    BASE_URL = Configs.base_url
    API_VERSION = Configs.api_version
    default_headers = {"Content-Type": "application/json"}

    @classmethod
    def get(cls, base_url, endpoint, **kwargs):
        """
        Method which executes GET request on specified endpoint
        :param base_url: url to which request should be sent
        :param endpoint: endpoint to which request should be sent
        :param \*\*kwargs: Optional arguments that ``request`` takes
        :return: requests.Response object
        """
        log('Sending GET url: %s headers: %s.' % (base_url + endpoint, kwargs['headers']))
        response = requests.get(base_url + endpoint, headers=kwargs["headers"])
        log('Received "%s".' % response)
        return response

    @classmethod
    def post(cls, base_url, endpoint, data, **kwargs):
        """
        Method which executes POST request on specified endpoint
        :param base_url: url to which request should be sent
        :param endpoint: endpoint to which request should be sent
        :param data: (dict) which should be sent in request body to create new contact
        :param \*\*kwargs: Optional arguments that ``request`` takes.
        :return: requests.Response object
        """
        log('Sending POST url: %s headers: %s. Body: %s' % (base_url + endpoint, kwargs['headers'], data))
        response = requests.post(base_url + endpoint, data=json.dumps(data), headers=cls.default_headers)
        log('Received "%s".' % response)
        return response

    @classmethod
    def delete(cls, base_url, endpoint, **kwargs):
        """
        Method which executes DELETE request on specified endpoint
        :param base_url: url to which request should be sent
        :param endpoint: endpoint to which request should be sent
        :param \*\*kwargs: Optional arguments that ``request`` takes.
        :return: requests.Response object
        """
        log('Sending DELETE url: %s headers: %s.' % (base_url + endpoint, kwargs['headers']))
        response = requests.delete(base_url + endpoint)
        log('Received "%s".' % response)
        return response

    @classmethod
    def put(cls, base_url, endpoint, data, **kwargs):
        """
        Method which executes PUT request on specified endpoint
        :param base_url: url to which request should be sent
        :param endpoint: endpoint to which request should be sent
        :param data: (dict) which should be sent in request body to update contact info
        :param \*\*kwargs: Optional arguments that ``request`` takes.
        :return: requests.Response object
        """
        log('Sending PUT url: %s headers: %s. Body: %s' % (base_url + endpoint, kwargs['headers'], data))
        response = requests.put(base_url + endpoint, data=json.dumps(data), headers=cls.default_headers)
        log('Received "%s".' % response)
        return response

    @classmethod
    def patch(cls, base_url, endpoint, data, **kwargs):
        """
        Method which executes PATCH request on specified endpoint
        :param base_url: url to which request should be sent
        :param endpoint: endpoint to which request should be sent
        :param data: (dict) which should be sent in request body to partial update of contact's info
        :param \*\*kwargs: Optional arguments that ``request`` takes.
        :return: requests.Response object
        """
        log('Sending PATCH url: %s headers: %s. Body: %s' % (base_url + endpoint, kwargs['headers'], data))
        response = requests.patch(base_url + endpoint, data=json.dumps(data), headers=cls.default_headers)
        log('Received "%s".' % response)
        return response
