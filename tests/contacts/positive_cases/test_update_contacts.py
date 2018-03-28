import pytest
from tests.contacts.test_base_contacts import TestBaseContacts
from configs.configs import Configs


# FIXTURE IS USED TO ADD AND DELETE CONTACT BEFORE EACH CASE
@pytest.mark.usefixtures("add_contact_before_and_delete_after")
@pytest.mark.skipif(Configs.api_version != '/api/v1', reason='First api version should be for scripts execution')
class TestUpdateContacts(TestBaseContacts):

    @pytest.allure.story("Update contact feature")
    @pytest.allure.testcase('Positive: PUT request to update info of contact')
    def test_full_contact_update(self, updated_contact_data):
        id_of_user_to_be_updated = self.contact_helpers.get_id_of_last_added_user()
        put_response = self.contacts_api.put_contact(updated_contact_data, user_id=id_of_user_to_be_updated)
        assert put_response.status_code == 200, 'Status code is incorrect'
        assert put_response.reason == 'OK', 'Status message is incorrect'
        assert self.contact_helpers.check_values_in_response_body(put_response.content,
                                                                  updated_contact_data.values()), \
            "Content doesn't contain correct value of contacts"

        # check that user was updated
        get_response = self.contacts_api.get_contact(user_id=id_of_user_to_be_updated)
        assert get_response.status_code == 200, 'Status code is incorrect'
        assert self.contact_helpers.check_values_in_response_body(put_response.content,
                                                                  updated_contact_data.values()),\
            "Content doesn't contain correct value of contacts"

    @pytest.allure.story("Update contact feature")
    @pytest.allure.testcase('Positive: PATCH request to partial update of contact info')
    def test_partial_contact_update(self, partial_updated_contact_data):
        id_of_user_to_be_updated = self.contact_helpers.get_id_of_last_added_user()
        patch_response = self.contacts_api.patch_contact(partial_updated_contact_data,
                                                            user_id=id_of_user_to_be_updated)
        assert patch_response.status_code == 200, 'Status code is incorrect'
        assert patch_response.reason == 'OK', 'Status message is incorrect'
        assert self.contact_helpers.check_values_in_response_body(
            patch_response.content, partial_updated_contact_data.values()), \
            "Content doesn't contain correct value of contacts"

        # check that user was updated
        get_response = self.contacts_api.get_contact(user_id=id_of_user_to_be_updated)
        assert get_response.status_code == 200, 'Status code is incorrect'
        assert self.contact_helpers.check_values_in_response_body(
            patch_response.content, partial_updated_contact_data.values()), \
            "Content doesn't contain correct value of contacts"
