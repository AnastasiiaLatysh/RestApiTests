import pytest
from api.contacts.contacts_api import ContactsApi
import json
from api.contacts.contacts_helper import ContactHelper


@pytest.fixture(scope='session')
def contacts_api():
    return ContactsApi()


@pytest.fixture(scope='session')
def contacts_helper():
    return ContactHelper()


@pytest.fixture
def add_contact_fixture(contact_data, contacts_api):
    # add contact before test method
    contacts_api.post_contact(contact_data)


@pytest.fixture
def delete_contact_fixture(contacts_helper, contacts_api):
    # get amount of users before test execution
    amount_of_users_before = contacts_helper.get_amount_of_contacts()
    yield
    # delete contact after test method if user was added at the beginning of the test
    if amount_of_users_before + 1 == contacts_helper.get_amount_of_contacts():
        contacts_api.delete_contact()


@pytest.fixture
def add_contact_before_and_delete_after(add_contact_fixture, delete_contact_fixture, contacts_api):
    # add contact before test method
    add_contact_fixture
    yield
    # delete contact after test method
    contacts_api.delete_contact()


# [Test Data fixtures]
@pytest.fixture(scope="session")
def contact_data():
    with open(ContactsApi.test_data_folder + "contact_test_data.json") as contact_data:
        yield json.load(contact_data)["default_data"]


@pytest.fixture(scope="session")
def updated_contact_data():
    with open(ContactsApi.test_data_folder + "contact_test_data.json") as contact_data:
            yield json.load(contact_data)["updated_data"]


@pytest.fixture(scope="session")
def partial_updated_contact_data():
    with open(ContactsApi.test_data_folder + "contact_test_data.json") as contact_data:
            yield json.load(contact_data)["partial_updated_data"]
