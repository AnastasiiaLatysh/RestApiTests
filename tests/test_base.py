# -*- coding: utf-8 -*-
""" TODO Этот файл не должен находиться здесь. Обычно создается отдельная директория lib содержащая код используемый в
тестах но к тестам не относящийся
"""


class TestBase:  # TODO Используется старые классы. Не используй никогда кроме как при поддержке старых проектов, тут по видимому должно было быть наследование от unittest.TestCase
    """
    Base class for all api resources
    """
    # TODO По видимому клас предполагался абстрактным. Посмотри в сторону библиотеки abc
    @classmethod
    def setup_class(cls):
        print("Base setup for all api resources")

    @classmethod
    def teardown_class(cls):
        print("Base tear down for api all resources")
