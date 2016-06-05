# -*- coding: UTF-8 -*-

from __future__ import unicode_literals

from pdepou.blog.models import Post

from django.test import Client

from .test_base import BaseTest


class PostClient(BaseTest):
    """
    Class that tests contact app urls
    """

    def setUp(self):
        self.client = Client()

    def test_post_list_url(self):
        response = self.client.get('/')
        assert response.status_code == 200

    def test_post_get_url(self):
        response = self.client.get('blog/post/?post_id=x')
        assert response.status_code == 404

    def test_post_post_url(self):
        response = self.client.post('blog/post/', {'name': 'Zelda',
                                                           'email': '',
                                                           'text': ''})
        assert response.status_code == 404
