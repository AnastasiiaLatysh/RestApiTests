from tests.test_base import TestBase
from api.contacts.contacts_helpers import ContactHelpers


class TestBaseContacts(TestBase):

    @classmethod
    def setup_class(cls):
        cls.contact_helpers = ContactHelpers
        print("set up contacts")

    @classmethod
    def teardown_class(cls):
        print("tear down contacts")
