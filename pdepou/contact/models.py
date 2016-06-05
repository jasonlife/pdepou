# -*- coding: UTF-8 -*-

from __future__ import unicode_literals

from pdepou.core.models import BaseModel

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Contact(BaseModel):
    """
    Class that represents the blog contacts. A contact is a
    person who sends a message or write a comment in a post
    """
    name = models.CharField(max_length=200)
    email = models.EmailField()

    @classmethod
    def check_contact(cls, name, email):
        """
        Check if exist a contact with the name and email specified
        If not exists create one
        :param name: Contact name to check
        :param email: Contact email to check
        :return: The existing o new contact
        """
        try:
            return Contact.objects.get(name=name, email=email)
        except Contact.DoesNotExist:
            return Contact.objects.create(name=name, email=email)

    def __str__(self):
        return '{0} ({1})'.format(self.name, self.email)

    class Meta:
        verbose_name = 'contact'
        verbose_name_plural = 'contacts'
        ordering = ['created']


@python_2_unicode_compatible
class Message(BaseModel):
    """
    Class that represents the messages sended
    by users using the contact form
    """
    text = models.TextField()
    contact = models.ForeignKey(Contact, on_delete=models.PROTECT)

    def __str__(self):
        return '{0} - {1}'.format(self.created, self.contact)

    class Meta:
        verbose_name = 'message'
        verbose_name_plural = 'messages'
        ordering = ['created']
