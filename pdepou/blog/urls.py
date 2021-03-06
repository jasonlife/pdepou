# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from .views import PostListView, PostView

urlpatterns = [
    url(regex=r'^$', view=PostListView.as_view(), name='post-list'),
    url(regex=r'^blog/post/$', view=PostView.as_view(), name='post-detail')
]
