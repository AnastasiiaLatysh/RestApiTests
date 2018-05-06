import pytest
from tests.contacts.test_base_contacts import TestBaseContacts
from configs.config import Config


@pytest.mark.usefixtures("add_contact_before_and_delete_after")
@pytest.mark.skipif(Config.api_version != '/api/v1', reason='First api version should be for scripts execution')
class TestDeleteNonExistentUser(TestBaseContacts):

    @pytest.allure.story("Delete contact feature")
    @pytest.allure.testcase('Negative: DELETE request to delete contact which doesn\'t exist - verify 404')
    def test_delete_nonexistent_contact(self):
        # check response code and reason for DELETE with empty data
        post_response = self.contacts_api.delete_contact(self.contact_helpers.get_nonexistent_contact_id())
        assert post_response.status_code == 404, 'Status code is incorrect'
        assert post_response.reason == 'Not Found', 'Status message is incorrect'
