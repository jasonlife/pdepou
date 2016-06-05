# -*- coding: UTF-8 -*-

from __future__ import unicode_literals

from django.db import models


class BaseModel(models.Model):
    """
    Abstact base class model that provides
    name, created and modified fields
    """
    created = models.DateTimeField(auto_now=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
