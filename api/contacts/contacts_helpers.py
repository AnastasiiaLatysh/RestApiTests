# -*- coding: utf-8 -*-
from api.base_helpers import BaseHelpers
from api.base_api import BaseApi
from configs.configs import Configs
from api.contacts.contacts_data_generation import ContactsDataGeneration


class ContactHelpers(BaseHelpers):  # TODO Не согласен с названием класса. Это просто следующий слой ContactAPI
    """
    Class which contains helpers for manipulating contacts endpoint
    """

    base_contacts_endpoint = Configs.base_contacts_endpoint

    @classmethod
    def get_response_data(cls):
        try:
            response_data = BaseHelpers.parse_response_json(BaseApi.get(BaseApi.BASE_URL,
                                                                        cls.base_contacts_endpoint,
                                                                        headers=BaseApi.default_headers),
                                                            'data')
            return response_data
        except KeyError:
            raise KeyError("There is no 'data' in returned response")

    @classmethod
    def get_amount_of_contacts(cls):
        return len(cls.get_response_data())

    @classmethod
    def get_id_of_last_added_user(cls):
        """
        Method which executes GET request on contacts api endpoint and
        get id of last added user from content of response
        :return: (int) id of last added user
        """
        return cls.get_response_data()[len(cls.get_response_data()) - 1]["id"]

    @classmethod
    def get_first_name_of_last_added_user(cls):
        """
        Method which executes GET request on contacts api endpoint and
        get firstName of last added user from content of response
        :return: (str) firstName of last added user
        """
        return cls.get_response_data()[len(cls.get_response_data()) - 1]["info"]["firstName"]

    @classmethod
    def get_last_name_of_last_added_user(cls):
        """
        Method which executes GET request on contacts api endpoint and
        get lastName of last added user from content of response
        :return: (str) lastName of last added user
        """
        return cls.get_response_data()[len(cls.get_response_data()) - 1]["info"]["lastName"]

    @classmethod
    def get_email_of_last_added_user(cls):
        """
        Method which executes GET request on contacts api endpoint and
        get email of last added user from content of response
        :return: (str) email of last added user
        """
        return cls.get_response_data()[len(cls.get_response_data()) - 1]["info"]["email"]

    @classmethod
    def get_contacts_ids(cls):
        """
        Method which executes GET request on contacts api endpoint and
        get ids of all existent contacts from content of response
        :return: (list) nonexistent ids of contacts
        """
        data = cls.get_response_data()
        nonexistent_ids = []
        for item in data:
            try:
                nonexistent_ids.append(int(item['id']))
            except KeyError:
                continue
        return nonexistent_ids

    @classmethod
    def get_nonexistent_contact_id(cls):
        """
        Method which executes GET request on contacts api endpoint and
        get id of nonexistent contact from content of response
        :return: (int) id of nonexistent contact
        """
        data = cls.get_contacts_ids()
        attempt = 0
        while attempt < 100:
            nonexistent_id = ContactsDataGeneration.generate_random_integer()
            if nonexistent_id not in data:
                return nonexistent_id
            else:
                attempt += 1
