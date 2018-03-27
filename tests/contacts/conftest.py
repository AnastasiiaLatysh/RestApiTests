import pytest
from api.base_helpers import BaseHelpers
from api.contacts.contacts_api import ContactsApi
import json
from api.contacts.contacts_helpers import ContactHelpers


@pytest.fixture()
def add_contact_fixture(contact_data):
    # add contact before test method
    response = ContactsApi.post_contact(contact_data)
    BaseHelpers.wait_until_condition_will_be_true(response.status_code == 201, 'adding contact')


@pytest.yield_fixture()
def delete_contact_fixture():
    # get amount of users before test execution
    amount_of_users_before = ContactHelpers.get_amount_of_contacts()
    yield
    # delete contact after test method if user was added at the beginning of the test
    if amount_of_users_before + 1 == ContactHelpers.get_amount_of_contacts():
        response = ContactsApi.delete_contact()
        BaseHelpers.wait_until_condition_will_be_true(response.status_code == 200)


@pytest.yield_fixture()
def add_contact_before_and_delete_after(add_contact_fixture, delete_contact_fixture):
    # add contact before test method
    add_contact_fixture
    yield
    # delete contact after test method
    response = ContactsApi.delete_contact()
    BaseHelpers.wait_until_condition_will_be_true(response.status_code == 200)


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
