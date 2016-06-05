# -*- coding: UTF-8 -*-

from __future__ import unicode_literals, absolute_import

from pdepou.core.models import BaseModel
from pdepou.contact.models import Contact

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


class PostManager(models.Manager):
    """
    Manager that allows get the published posts
    """
    def published(self, **kwargs):
        return self.filter(published=True, **kwargs).order_by('-created')


@python_2_unicode_compatible
class Post(BaseModel):
    """
    Class that represents the blog's posts
    """
    name = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)
    technology = models.CharField(max_length=200)
    published = models.BooleanField(default=True)
    image = models.ImageField()

    # Add the custom model manager
    objects = PostManager()

    def __str__(self):
        return '{}'.format(self.name)

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'
        ordering = ['created']


@python_2_unicode_compatible
class Comment(BaseModel):
    """
    Class that represents the different post's
    comments written by different contacts
    """
    text = models.TextField()
    post = models.ForeignKey(Post, related_name='comments',
                             on_delete=models.CASCADE)
    contact = models.ForeignKey(Contact, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return '{0} - {1}'.format(self.post, self.contact)

    class Meta:
        verbose_name = 'comment'
        verbose_name_plural = 'comments'
        ordering = ['created']
