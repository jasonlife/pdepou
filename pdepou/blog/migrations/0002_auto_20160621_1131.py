# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-21 09:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_first_migration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='contact',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='contact.Contact'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='created',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='created',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
