from api.base_api import BaseApi
from configs.config import Config
from api.contacts.contacts_helper import ContactHelper


class ContactsApi(BaseApi):
    """
    Class which represents api for contacts endpoint
    """

    base_contacts_endpoint = ContactHelper.base_contacts_endpoint
    test_data_folder = Config.path_to_main_dir + "/tests/contacts/"

    def __init__(self):
        self.contact_helper = ContactHelper()
        super(ContactsApi, self).__init__()

    def get_contact(self, user_id=None, user_query_params=None):
        """
        Method which executes GET request on contacts endpoint
        By default get information of all existing users
        :param user_id: id of user whom information is needed to be got
        :param user_query_params: query params of user whom information needed to be got
        :param \*\*kwargs: Optional arguments that ``request`` takes
        :return: requests.Response object
        """
        if user_id is not None:
            return self.get(self.BASE_URL, self.base_contacts_endpoint + "/" + str(user_id),
                            headers=self.default_headers)
        elif user_query_params:
            return self.get(self.BASE_URL, self.base_contacts_endpoint + "?" + str(user_query_params),
                            headers=self.default_headers)
        else:
            return self.get(self.BASE_URL, self.base_contacts_endpoint, headers=self.default_headers)

    def post_contact(self, data):
        """
        Method which executes POST request on contacts endpoint
        :param data: data which should be sent in request dody to create new contact
        :param \*\*kwargs: Optional arguments that ``request`` takes.
        :return: requests.Response object
        """
        return self.post(self.BASE_URL, self.base_contacts_endpoint, data, headers=self.default_headers)

    def put_contact(self, data, user_id=None):
        """
        Method which executes PUT request on contacts endpoint
        By default update info of  last added user from DB
        :param data: path to json file which should be sent in body of request
        :param user_id: id of user which should be updated
        :param \*\*kwargs: Optional arguments that ``request`` takes.
        :return: requests.Response object
        """
        if user_id is None:
            return self.put(self.BASE_URL, self.base_contacts_endpoint + '/' +
                            str(self.contact_helper.get_id_of_last_added_user()), data,
                            headers=self.default_headers)
        else:
            return self.put(self.BASE_URL, self.base_contacts_endpoint + '/' + str(user_id), data,
                            headers=self.default_headers)

    def patch_contact(self, data, user_id=None):
        """
        Method which executes PUT request on contacts endpoint
        By default update info of  last added user from DB
        :param data: path to json file which should be sent in body of request
        :param user_id: id of user which should be updated
        :param \*\*kwargs: Optional arguments that ``request`` takes.
        :return: requests.Response object
        """
        if user_id is None:
            return self.patch(self.BASE_URL, self.base_contacts_endpoint + '/' +
                              str(self.contact_helper.get_id_of_last_added_user()),
                              data=data, headers=self.default_headers)
        else:
            return self.patch(self.BASE_URL, self.base_contacts_endpoint + '/' + str(user_id), data=data,
                              headers=self.default_headers)

    def delete_contact(self, user_id=None):
        """
        Method which executes DELETE request on contacts endpoint
        By default delete last added user from DB
        :param user_id: id of user which should be deleted
        :param \*\*kwargs: Optional arguments that ``request`` takes.
        :return: requests.Response object
        """
        if user_id is None:
            return self.delete(self.BASE_URL, self.base_contacts_endpoint + '/' +
                               str(self.contact_helper.get_id_of_last_added_user()),
                               headers=self.default_headers)
        else:
            return self.delete(self.BASE_URL, self.base_contacts_endpoint + '/' +
                               str(user_id), headers=self.default_headers)
