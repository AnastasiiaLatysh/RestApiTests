import pytest
from tests.contacts.test_base_contacts import TestBaseContacts
from api.contacts.contacts_data_generation import ContactsDataGeneration
from configs.configs import Configs


# FIXTURE IS USED TO DELETE CONTACT AFTER EACH TEST IN CASE USER WITH INVALID DATA WAS ADDED
@pytest.mark.usefixtures("delete_contact_fixture")
@pytest.mark.skipif(Configs.api_version != '/api/v1', reason='First api version should be for scripts execution')
class TestAddWithIncorrectData(TestBaseContacts):

    @pytest.allure.story("Add contact feature")
    @pytest.allure.testcase('Negative: POST request to add new contact - verify 404')
    @pytest.mark.xfail()
    def test_add_contact_with_empty_data(self):
        # check response code and reason for POST with empty data
        post_response = self.contacts_api.post_contact(ContactsDataGeneration.generate_empty_data())
        assert post_response.status_code == 404, 'Status code is incorrect'
        assert post_response.reason == 'Not Found', 'Status message is incorrect'

    @pytest.allure.story("Add contact feature")
    @pytest.allure.testcase('Negative: POST request to add new contact - verify 404')
    @pytest.mark.xfail()
    @pytest.mark.parametrize("with_empty_filed", [ContactsDataGeneration.generate_data(empty_name=True),
                                                  ContactsDataGeneration.generate_data(empty_last_name=True)],
                             ids=["empty_name", "empty_last_name"])
    def test_add_contact_with_empty_field(self,  with_empty_filed):
        # check response code and reason for POST with empty field
        post_response = self.contacts_api.post_contact(with_empty_filed)
        assert post_response.status_code == 404, 'Status code is incorrect'
        assert post_response.reason == 'Not Found', 'Status message is incorrect'

    @pytest.allure.story("Add contact feature")
    @pytest.allure.testcase('Negative: POST request to add new contact - verify 404')
    @pytest.mark.xfail()
    @pytest.mark.parametrize("without_needed_symbols", ["test_email.com", "email@com", ""],
                             ids=["without_@", "without_dot", "empty email"])
    def test_add_contact_with_incorrect_data(self, without_needed_symbols, ):
        # check response code and reason for POST with incorrect or empty email
        data = ContactsDataGeneration.generate_data()
        data['email'] = without_needed_symbols
        post_response = self.contacts_api.post_contact(data)
        assert post_response.status_code == 404, 'Status code is incorrect'
        assert post_response.reason == 'Not Found', 'Status message is incorrect'
