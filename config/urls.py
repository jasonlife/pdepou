# -*- coding: UTF-8 -*-

from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    # Fake admin
    url(r'^admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),

    # Django Admin, use {% url 'admin:index' %}
    url(r'{}'.format(settings.ADMIN_URL), include(admin.site.urls)),

    # Internal apps
    url(r'^', include('pdepou.blog.urls', namespace='blog')),
    url(r'^contact/', include('pdepou.contact.urls', namespace='contact')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
