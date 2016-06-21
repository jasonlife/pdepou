# -*- coding: UTF-8 -*-

from __future__ import unicode_literals

import os

from django.test import Client

from pdepou.blog.models import Post
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
        post = Post.objects.create(name='The legend of Zelda',
                                   slug='zelda',
                                   technology='Nintendo')
        modal = 'pdepou/templates/blog/modals/_{}.html'.format(post.slug)
        open(modal, 'w')
        response = self.client.get('/blog/post/', {'post_id': post.id},
                                   HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        os.remove(modal)
        post.delete()
        assert response.status_code == 200

    def test_post_post_url(self):
        post = Post.objects.create(name='The legend of Zelda',
                                   slug='zelda',
                                   technology='Nintendo')
        response = self.client.post('/blog/post/', {'name': 'Navi',
                                                    'email': 'navi@hirule.zel',
                                                    'text': 'Hey Link!',
                                                    'post_id': post.id},
                                    HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        post.delete()
        assert response.status_code == 200
