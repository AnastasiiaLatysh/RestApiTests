class TestBase:
    """
    Base class for all api resources
    """
    @classmethod
    def setup_class(cls):
        print("Base setup for all api resources")

    @classmethod
    def teardown_class(cls):
        print("Base tear down for api all resources")
