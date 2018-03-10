import pytest
from api.base_helpers import BaseHelpers
from api.contacts.contacts_api import ContactsApi
import json


@pytest.fixture(scope='class')
def contacts_api_fixture():
    return ContactsApi()


@pytest.fixture()
def add_contact_fixture(contacts_api_fixture, contact_data):
    # add contact before test method
    response = contacts_api_fixture.post_contact(contact_data)
    BaseHelpers.wait_until(response.status_code == 201)


@pytest.yield_fixture()
def delete_contact_fixture(contacts_api_fixture):
    # do nothing before test method
    yield
    # delete contact after test method
    response = contacts_api_fixture.delete_contact()
    BaseHelpers.wait_until(response.status_code == 200)


@pytest.yield_fixture()
def add_contact_before_and_delete_after(contacts_api_fixture, contact_data):
    # add contact before test method
    response = contacts_api_fixture.post_contact(contact_data)
    BaseHelpers.wait_until(response.status_code == 201)
    yield
    # delete contact after test method
    response = contacts_api_fixture.delete_contact()
    BaseHelpers.wait_until(response.status_code == 200)


# [Test Data fixtures]
@pytest.fixture(scope="class")
def contact_data(contacts_api_fixture):
    with open(contacts_api_fixture.test_data_folder + "contact_test_data.json") as contact_data:
        return json.load(contact_data)["default_data"]


@pytest.fixture(scope="class")
def updated_contact_data(contacts_api_fixture):
    with open(contacts_api_fixture.test_data_folder + "contact_test_data.json") as contact_data:
            return json.load(contact_data)["updated_data"]


@pytest.fixture(scope="class")
def partial_updated_contact_data(contacts_api_fixture):
    with open(contacts_api_fixture.test_data_folder + "contact_test_data.json") as contact_data:
            return json.load(contact_data)["partial_updated_data"]
