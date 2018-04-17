# -*- coding: utf-8 -*-
import configparser
import os


class Configs(object):  # TODO Имя класа в единственном числе
    """
    Class which stores config information
    """
    # create instance of config parser and begin read config file
    # TODO Все свойства этого класа должны обьявляться при инициализации класса
    parser = configparser.ConfigParser()
    parser.read(os.path.dirname(os.path.abspath(__file__)) + "/configs.conf")  # TODO дополнительно передавать значение при запуски через аргументы командной строки или переиенную среды. Потом -передавать в конструктор этого класса

    # read base url and contacts endpoint from configs
    base_url = parser.get('api_test_parameters', 'BASE_URL')
    api_version = parser.get('api_test_parameters', 'api_version')
    base_contacts_endpoint = api_version + parser.get('api_test_parameters', 'base_contacts_endpoint')

    # read paths
    path_to_main_dir = parser.get('paths', 'path_to_main_dir')
