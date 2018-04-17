# -*- coding: utf-8 -*-
import pytest
from tests.contacts.test_base_contacts import TestBaseContacts
from configs.configs import Configs


@pytest.mark.skipif(Configs.api_version != '/api/v1', reason='First api version should be for scripts execution')
class TestAddDeleteContacts(TestBaseContacts):  # TODO при использовании pytest не принято обьединять тесты в классы (только в случае legacy)

    @pytest.allure.story("Add contact feature")
    @pytest.allure.testcase('Positive: POST request to add new contact - verify 201'
                            'Created contact will be deleted after test script using delete_contact_fixture')
    @pytest.mark.usefixtures("delete_contact_fixture")
    def test_add_contact(self, contact_data):
        # check response code, reason and body for POST
        post_response = self.contacts_api.post_contact(contact_data)
        assert post_response.status_code == 201, 'Status code is incorrect'
        assert post_response.reason == 'Created', 'Status message is incorrect'
        assert self.contact_helpers.check_values_in_response_body(post_response.content, contact_data.values()), \
            'Content is incorrect'

    @pytest.allure.story("Delete contact feature")
    @pytest.allure.testcase('Positive: DELETE request to delete contact by id - verify 200'
                            'Contact was added before DELETE using add_contact_fixture')
    @pytest.mark.usefixtures("add_contact_fixture")
    def test_delete_contact(self, contact_data):
        # check response code, reason and body for DELETE
        id_of_user_to_be_deleted = self.contact_helpers.get_id_of_last_added_user()
        delete_response = self.contacts_api.delete_contact(userId=id_of_user_to_be_deleted)
        assert delete_response.status_code == 200, 'Status code is incorrect'
        assert delete_response.reason == 'OK', 'Status message is incorrect'
        assert self.contact_helpers.check_values_in_response_body(delete_response.content, contact_data.values()), \
            'Content is incorrect'

        # check that user was deleted
        get_response = self.contacts_api.get_contact(user_id=id_of_user_to_be_deleted)
        assert get_response.status_code == 404, 'Status code is incorrect'
        assert get_response.reason == 'Not Found', 'Status message is incorrect'
