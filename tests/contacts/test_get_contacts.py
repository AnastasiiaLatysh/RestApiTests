import pytest
from tests.contacts.test_base_contacts import TestBaseContacts


@pytest.mark.usefixtures("contacts_api_fixture", "add_contact_before_and_delete_after", "contact_data")
class TestGetContacts(TestBaseContacts):

    @pytest.allure.testcase('Positive: GET request to get info of all contacts'
                            'Contact was added before GET and will be deleted after')
    def test_get_all_contacts(self, contacts_api_fixture, contact_data):
        get_response = contacts_api_fixture.get_contact()
        assert get_response.status_code == 200, 'Status code is incorrect'
        assert get_response.reason == 'OK', 'Status message is incorrect'
        assert self.contact_helpers.check_values_in_response_body(get_response.content, contact_data.values()), \
            'Content doesn\'t contain correct value'

    @pytest.allure.testcase('Positive: GET request to get info of contact by id'
                            'Contact was added before GET and will be deleted after')
    def test_get_contact_by_id(self, contacts_api_fixture, contact_data):
        get_response = contacts_api_fixture.get_contact(user_id=contacts_api_fixture.get_id_of_last_added_user())
        assert get_response.status_code == 200, 'Status code is incorrect'
        assert get_response.reason == 'OK', 'Status message is incorrect'
        assert self.contact_helpers.check_values_in_response_body(get_response.content, contact_data.values()), \
            "Content doesn't contain correct value of contact with id {}".format(
                contacts_api_fixture.get_id_of_last_added_user())

    @pytest.allure.testcase('Positive: GET request to get info of contact by query params'
                            'Contact was added before GET and will be deleted after')
    def test_get_contact_by_query_params(self, contacts_api_fixture, contact_data):
        get_response = contacts_api_fixture.get_contact(user_query_params="firstName={}&email={}".format(
            contacts_api_fixture.get_first_name_of_last_added_user(),
            contacts_api_fixture.get_email_of_last_added_user()))
        assert get_response.status_code == 200, 'Status code is incorrect'
        assert get_response.reason == 'OK', 'Status message is incorrect'
        assert self.contact_helpers.check_values_in_response_body(get_response.content, contact_data.values()), \
            "Content doesn't contain correct value of contact with id {}".format(
                contacts_api_fixture.get_id_of_last_added_user())
