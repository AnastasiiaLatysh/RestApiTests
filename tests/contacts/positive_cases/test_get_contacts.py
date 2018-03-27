import pytest
from tests.contacts.test_base_contacts import TestBaseContacts


# FIXTURE IS USED TO ADD AND DELETE CONTACT BEFORE EACH CASE
@pytest.mark.usefixtures("add_contact_before_and_delete_after")
class TestGetContacts(TestBaseContacts):

    @pytest.allure.testcase('Positive: GET request to get info of all contacts')
    def test_get_all_contacts(self, contact_data):
        get_response = self.contacts_api.get_contact()
        assert get_response.status_code == 200, 'Status code is incorrect'
        assert get_response.reason == 'OK', 'Status message is incorrect'
        assert self.contact_helpers.check_values_in_response_body(get_response.content, contact_data.values()), \
            'Content doesn\'t contain correct value'

    @pytest.allure.testcase('Positive: GET request to get info of contact by id')
    def test_get_contact_by_id(self, contact_data):
        get_response = self.contacts_api.get_contact(user_id=self.contact_helpers.get_id_of_last_added_user())
        assert get_response.status_code == 200, 'Status code is incorrect'
        assert get_response.reason == 'OK', 'Status message is incorrect'
        assert self.contact_helpers.check_values_in_response_body(get_response.content, contact_data.values()), \
            "Content doesn't contain correct value of contact with id {}".format(
                self.contact_helpers.get_id_of_last_added_user())

    @pytest.allure.testcase('Positive: GET request to get info of contact by query params')
    def test_get_contact_by_query_params(self, contact_data):
        get_response = self.contacts_api.get_contact(user_query_params="firstName={}&email={}".format(
            self.contact_helpers.get_first_name_of_last_added_user(),
            self.contact_helpers.get_email_of_last_added_user()))
        assert get_response.status_code == 200, 'Status code is incorrect'
        assert get_response.reason == 'OK', 'Status message is incorrect'
        assert self.contact_helpers.check_values_in_response_body(get_response.content, contact_data.values()), \
            "Content doesn't contain correct value of contact with id {}".format(
                self.contact_helpers.get_id_of_last_added_user())
