from api.base_api import BaseApi
from api.base_helpers import parse_response_json
from api.contacts.contacts_data_generation import ContactsDataGeneration
from configs.config import Config


class ContactHelper(object):
    """
    Class which contains helpers for manipulating contacts endpoint
    """

    base_contacts_endpoint = Config.base_contacts_endpoint

    def get_response_data(self):
        try:
            base_api = BaseApi()
            response_data = parse_response_json(base_api.get(base_api.BASE_URL, self.base_contacts_endpoint,
                                                             headers=base_api.default_headers), 'data')
            return response_data
        except KeyError:
            raise KeyError("There is no 'data' in returned response")

    def get_amount_of_contacts(self):
        return len(self.get_response_data())

    def get_id_of_last_added_user(self):
        """
        Method which executes GET request on contacts api endpoint and
        get id of last added user from content of response
        :return: (int) id of last added user
        """
        response_data = self.get_response_data()
        return response_data[len(response_data) - 1]["id"]

    def get_first_name_of_last_added_user(self):
        """
        Method which executes GET request on contacts api endpoint and
        get firstName of last added user from content of response
        :return: (str) firstName of last added user
        """
        return self.get_response_data()[len(self.get_response_data()) - 1]["info"]["firstName"]

    def get_last_name_of_last_added_user(self):
        """
        Method which executes GET request on contacts api endpoint and
        get lastName of last added user from content of response
        :return: (str) lastName of last added user
        """
        return self.get_response_data()[len(self.get_response_data()) - 1]["info"]["lastName"]

    def get_email_of_last_added_user(self):
        """
        Method which executes GET request on contacts api endpoint and
        get email of last added user from content of response
        :return: (str) email of last added user
        """
        return self.get_response_data()[len(self.get_response_data()) - 1]["info"]["email"]

    def get_contacts_ids(self):
        """
        Method which executes GET request on contacts api endpoint and
        get ids of all existent contacts from content of response
        :return: (list) nonexistent ids of contacts
        """
        data = self.get_response_data()
        nonexistent_ids = []
        for item in data:
            try:
                nonexistent_ids.append(int(item['id']))
            except KeyError:
                continue
        return nonexistent_ids

    def get_nonexistent_contact_id(self):
        """
        Method which executes GET request on contacts api endpoint and
        get id of nonexistent contact from content of response
        :return: (int) id of nonexistent contact
        """
        data = self.get_contacts_ids()
        attempt = 0
        while attempt < 100:
            nonexistent_id = ContactsDataGeneration.generate_random_integer()
            if nonexistent_id not in data:
                return nonexistent_id
            else:
                attempt += 1
