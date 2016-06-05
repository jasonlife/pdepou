# -*- coding: UTF-8 -*-

from __future__ import unicode_literals

from test_plus import TestCase


class BaseTest(TestCase):
    """
    Class for inheritance in our tests. Base to
    integration tests
    """

    @classmethod
    def setUpClass(cls):
        # Here can put data in DB to use in all child classes
        super(BaseTest, cls).setUpClass()
