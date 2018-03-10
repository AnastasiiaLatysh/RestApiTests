import pytest
from tests.contacts.test_base_contacts import TestBaseContacts


@pytest.mark.usefixtures("contacts_api_fixture", "contact_data")
class TestAddDeleteContacts(TestBaseContacts):

    @pytest.allure.testcase('Positive: POST request to add new contact - verify 201'
                            'Created contact will be deleted after test script using delete_contact_fixture')
    def test_add_contact(self, contacts_api_fixture, contact_data, delete_contact_fixture):
        post_response = contacts_api_fixture.post_contact(contact_data)
        assert post_response.status_code == 201, 'Status code is incorrect'
        assert post_response.reason == 'Created', 'Status message is incorrect'
        assert self.contact_helpers.check_values_in_response_body(post_response.content, contact_data.values()), \
            'Content is incorrect'

    @pytest.allure.testcase('Positive: DELETE request to delete contact by id - verify 200'
                            'Contact was added before deleting using add_contact_fixture')
    def test_delete_contact(self, contacts_api_fixture, contact_data, add_contact_fixture):
        id_of_user_to_be_deleted = contacts_api_fixture.get_id_of_last_added_user()
        delete_response = contacts_api_fixture.delete_contact(userId=id_of_user_to_be_deleted)
        assert delete_response.status_code == 200, 'Status code is incorrect'
        assert delete_response.reason == 'OK', 'Status message is incorrect'
        assert self.contact_helpers.check_values_in_response_body(delete_response.content, contact_data.values()), \
            'Content is incorrect'

        # check that user was deleted
        get_response = contacts_api_fixture.get_contact(user_id=id_of_user_to_be_deleted)
        assert get_response.status_code == 404, 'Status code is incorrect'
        assert get_response.reason == 'Not Found', 'Status message is incorrect'
