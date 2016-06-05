# -*- coding: UTF-8 -*-

from __future__ import unicode_literals

import pytest
from mock import patch

from ..models import Post


@pytest.mark.unit
@pytest.mark.django_db
class TestPost(object):
    """
    Post unit test
    """

    @patch('shutil.copy2')
    def test_save_without_pk(self, m_shutil):
        post = Post(name='Test post', slug='test_post')
        post.save()
        m_shutil.assert_called_once()

    @patch('shutil.copy2')
    def test_save_with_pk(self, m_shutil):
        post = Post.objects.create(id='1', name='Test pos', slug='test_post')
        m_shutil.assert_not_called()
