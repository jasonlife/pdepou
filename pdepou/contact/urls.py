# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from .views import ContactView

urlpatterns = [
    url(regex=r'^contact/$', view=ContactView.as_view(), name='contact-detail')
]
