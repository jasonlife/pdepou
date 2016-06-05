# -*- coding: UTF-8 -*-

from __future__ import unicode_literals

from django.contrib import admin

from .models import Contact, Message


class ContactAdmin(admin.ModelAdmin):
    list_filter = ('created',)
    list_display = ('created', 'name', 'email')


class MessageAdmin(admin.ModelAdmin):
    list_filter = ('created',)
    list_display = ('created', 'contact', 'text')


admin.site.register(Contact, ContactAdmin)
admin.site.register(Message, MessageAdmin)
