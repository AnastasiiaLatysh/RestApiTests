from api.base_helpers import BaseHelpers


class TestBase:

    @classmethod
    def setup_class(cls):
        print("Base setup for all resources")

    @classmethod
    def teardown_class(cls):
        print("Base tear down for all resources")
