# -*- coding: UTF-8 -*-

from __future__ import unicode_literals

from django.test import Client

from .test_base import BaseTest


class ContactClient(BaseTest):
    """
    Class that tests contact app urls
    """

    def setUp(self):
        self.client = Client()

    def test_contact_post_url(self):
        response = self.client.post('/contact/contact/',
                                    {'name': 'Ganondorf',
                                     'email': 'ganon@hyrule.zel',
                                     'text': 'I welcome the hero time'},
                                    HTTP_X_REQUESTED_WITH='XMLHttpRequest'
                                    )
        assert response.status_code == 200
