import string
import random


class ContactsDataGeneration(object):

    @classmethod
    def generate_data(cls, empty_name=False, empty_last_name=False, max_string_len=10):
        email = ''.join(random.choice(string.ascii_letters) for _ in range(max_string_len)) + "@gmail.com"
        name = ''
        last_name = ''
        if not empty_name and not empty_last_name:
            name = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(max_string_len))
            last_name = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(max_string_len))
        elif not empty_last_name and empty_name:
            last_name = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(max_string_len))
        elif not empty_name and empty_last_name:
            name = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(max_string_len))

        data = {"email": email,
                "firstName": name,
                "lastName": last_name}
        return data

    @classmethod
    def generate_empty_data(cls):
        data = {"email": "",
                "firstName": "",
                "lastName": ""}
        return data

    @classmethod
    def generate_random_integer(cls, begin=0, end=10000):
        return random.randint(begin, end)
