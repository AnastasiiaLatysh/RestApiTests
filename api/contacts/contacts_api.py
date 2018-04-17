# -*- coding: utf-8 -*-
from api.base_api import BaseApi
from api.contacts.contacts_helpers import ContactHelpers
from configs.configs import Configs


class ContactsApi(BaseApi):
    """
    Class which represents api for contacts endpoint
    """
    base_contacts_endpoint = ContactHelpers.base_contacts_endpoint
    test_data_folder = Configs.path_to_main_dir + "/api/contacts/"

    # TODO Необьяснимая любовь к классметодам. См. комментарий к базовому классу
    @classmethod
    def get_contact(cls, user_id=None, user_query_params=None, **kwargs):  # TODO нужны ли здесь kwargs?
        """
        Method which executes GET request on contacts endpoint
        By default get information of all existing users
        :param user_id: id of user whom information is needed to be got
        :param user_query_params: query params of user whom information needed to be got
        :param \*\*kwargs: Optional arguments that ``request`` takes
        :return: requests.Response object
        """
        if user_id is not None:
            return cls.get(cls.BASE_URL, cls.base_contacts_endpoint + "/" + str(user_id),
                           headers=cls.default_headers)
        elif user_query_params:
            return cls.get(cls.BASE_URL, cls.base_contacts_endpoint + "?" + str(user_query_params),
                           headers=cls.default_headers)
        else:
            return cls.get(cls.BASE_URL, cls.base_contacts_endpoint, headers=cls.default_headers)

    @classmethod
    def post_contact(cls, data, **kwargs):
        """
        Method which executes POST request on contacts endpoint
        :param data: data which should be sent in request dody to create new contact
        :param \*\*kwargs: Optional arguments that ``request`` takes.
        :return: requests.Response object
        """
        return cls.post(cls.BASE_URL, cls.base_contacts_endpoint, data, headers=cls.default_headers)

    @classmethod
    def put_contact(cls, data, user_id=None,  **kwargs):
        """
        Method which executes PUT request on contacts endpoint
        By default update info of  last added user from DB
        :param data: path to json file which should be sent in body of request
        :param user_id: id of user which should be updated
        :param \*\*kwargs: Optional arguments that ``request`` takes.
        :return: requests.Response object
        """
        if user_id is None:
            return cls.put(cls.BASE_URL, cls.base_contacts_endpoint + '/' +
                           str(ContactHelpers.get_id_of_last_added_user()), data,
                           headers=cls.default_headers)
        else:
            return cls.put(cls.BASE_URL, cls.base_contacts_endpoint + '/' + str(user_id), data,
                           headers=cls.default_headers)

    @classmethod
    def patch_contact(cls, data, user_id=None, **kwargs):
        """
        Method which executes PUT request on contacts endpoint
        By default update info of  last added user from DB
        :param data: path to json file which should be sent in body of request
        :param user_id: id of user which should be updated
        :param \*\*kwargs: Optional arguments that ``request`` takes.
        :return: requests.Response object
        """
        if user_id is None:
            return cls.patch(cls.BASE_URL, cls.base_contacts_endpoint + '/' +
                             str(ContactHelpers.get_id_of_last_added_user()),
                             data=data, headers=cls.default_headers)
        else:
            return cls.patch(cls.BASE_URL, cls.base_contacts_endpoint + '/' + str(user_id), data=data,
                             headers=cls.default_headers)

    @classmethod
    def delete_contact(cls, user_id=None, **kwargs):
        """
        Method which executes DELETE request on contacts endpoint
        By default delete last added user from DB
        :param user_id: id of user which should be deleted
        :param \*\*kwargs: Optional arguments that ``request`` takes.
        :return: requests.Response object
        """
        if user_id is None:
            return cls.delete(cls.BASE_URL, cls.base_contacts_endpoint + '/' +
                              str(ContactHelpers.get_id_of_last_added_user()),
                              headers=cls.default_headers)
        else:
            return cls.delete(cls.BASE_URL, cls.base_contacts_endpoint + '/' +
                              str(user_id), headers=cls.default_headers)
