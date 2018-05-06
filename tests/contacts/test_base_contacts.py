from api.contacts.contacts_helper import ContactHelper
from api.contacts.contacts_api import ContactsApi


class TestBaseContacts(object):

    @classmethod
    def setup_class(cls):
        print("set up contacts")
        cls.contacts_api = ContactsApi()
        cls.contact_helpers = ContactHelper()
        cls.base_helpers = ContactHelper()

    @classmethod
    def teardown_class(cls):
        print("tear down contacts")
