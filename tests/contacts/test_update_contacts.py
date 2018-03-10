import pytest
import allure
from tests.contacts.test_base_contacts import TestBaseContacts


@pytest.mark.usefixtures("contacts_api_fixture", "add_contact_before_and_delete_after")
class TestUpdateContacts(TestBaseContacts):

    @allure.testcase('Positive: PUT request to update info of contact'
                     'Contact was added before PUT and will be deleted after')
    def test_full_contact_update(self, contacts_api_fixture, updated_contact_data):
        id_of_user_to_be_updated = contacts_api_fixture.get_id_of_last_added_user()
        put_response = contacts_api_fixture.put_contact(updated_contact_data, user_id=id_of_user_to_be_updated)
        assert put_response.status_code == 200, 'Status code is incorrect'
        assert put_response.reason == 'OK', 'Status message is incorrect'
        assert self.contact_helpers.check_values_in_response_body(put_response.content, updated_contact_data.values()), \
            "Content doesn't contain correct value of contacts"

        # check that user was updated
        get_response = contacts_api_fixture.get_contact(user_id=id_of_user_to_be_updated)
        assert get_response.status_code == 200, 'Status code is incorrect'
        assert self.contact_helpers.check_values_in_response_body(put_response.content, updated_contact_data.values()), \
            "Content doesn't contain correct value of contacts"

    @pytest.allure.testcase('Positive: PATCH request to partial update of contact info'
                            'Contact was added before PATCH and will be deleted after')
    def test_partial_contact_update(self, contacts_api_fixture, partial_updated_contact_data):
        id_of_user_to_be_updated = contacts_api_fixture.get_id_of_last_added_user()
        patch_response = contacts_api_fixture.patch_contact(partial_updated_contact_data,
                                                            user_id=id_of_user_to_be_updated)
        assert patch_response.status_code == 200, 'Status code is incorrect'
        assert patch_response.reason == 'OK', 'Status message is incorrect'
        assert self.contact_helpers.check_values_in_response_body(
            patch_response.content, partial_updated_contact_data.values()), \
            "Content doesn't contain correct value of contacts"

        # check that user was updated
        get_response = contacts_api_fixture.get_contact(user_id=id_of_user_to_be_updated)
        assert get_response.status_code == 200, 'Status code is incorrect'
        assert self.contact_helpers.check_values_in_response_body(
            patch_response.content, partial_updated_contact_data.values()), \
            "Content doesn't contain correct value of contacts"
