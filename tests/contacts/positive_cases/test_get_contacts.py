import pytest
from tests.contacts.test_base_contacts import TestBaseContacts
from configs.config import Config
from api.base_helpers import check_values_in_response_body


# FIXTURE IS USED TO ADD AND DELETE CONTACT BEFORE EACH CASE
@pytest.mark.usefixtures("add_contact_before_and_delete_after")
@pytest.mark.skipif(Config.api_version != '/api/v1', reason='First api version should be for scripts execution')
class TestGetContacts(TestBaseContacts):

    @pytest.allure.story("Get contact feature")
    @pytest.allure.testcase('Positive: GET request to get info of all contacts')
    def test_get_all_contacts(self, contact_data):
        get_response = self.contacts_api.get_contact()
        assert get_response.status_code == 200, 'Status code is incorrect'
        assert get_response.reason == 'OK', 'Status message is incorrect'
        assert check_values_in_response_body(get_response.content, contact_data.values()), \
            'Content doesn\'t contain correct value'

    @pytest.allure.story("Get contact feature")
    @pytest.allure.testcase('Positive: GET request to get info of contact by id')
    def test_get_contact_by_id(self, contact_data):
        get_response = self.contacts_api.get_contact(user_id=self.contact_helpers.get_id_of_last_added_user())
        assert get_response.status_code == 200, 'Status code is incorrect'
        assert get_response.reason == 'OK', 'Status message is incorrect'
        assert check_values_in_response_body(get_response.content, contact_data.values()), \
            "Content doesn't contain correct value of contact with id {}".format(
                self.contact_helpers.get_id_of_last_added_user())

    @pytest.allure.story("Get contact feature")
    @pytest.allure.testcase('Positive: GET request to get info of contact by query params')
    def test_get_contact_by_query_params(self, contact_data):
        get_response = self.contacts_api.get_contact(user_query_params="firstName={}&email={}".format(
            self.contact_helpers.get_first_name_of_last_added_user(),
            self.contact_helpers.get_email_of_last_added_user()))
        assert get_response.status_code == 200, 'Status code is incorrect'
        assert get_response.reason == 'OK', 'Status message is incorrect'
        assert check_values_in_response_body(get_response.content, contact_data.values()), \
            "Content doesn't contain correct value of contact with id {}".format(
                self.contact_helpers.get_id_of_last_added_user())
