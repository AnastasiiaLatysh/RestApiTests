import configparser
import os


class Configs(object):
    """
    Class which stores config information
    """
    # create instance of config parser and begin read config file
    parser = configparser.ConfigParser()
    parser.read(os.path.dirname(os.path.abspath(__file__)) + "/configs.conf")

    # read base url and contacts endpoint from configs
    base_url = parser.get('api_test_parameters', 'BASE_URL')
    base_contacts_endpoint = parser.get('api_test_parameters', 'base_contacts_endpoint')
