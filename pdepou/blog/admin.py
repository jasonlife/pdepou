# -*- coding: UTF-8 -*-

from __future__ import unicode_literals

from django.contrib import admin

from .models import Comment, Post


class PostAdmin(admin.ModelAdmin):
    list_filter = ('created',)
    list_display = ('created', 'name', 'published')


class CommentAdmin(admin.ModelAdmin):
    list_filter = ('created',)
    list_display = ('created', 'post', 'contact')


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
