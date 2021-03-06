# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-09 17:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
            ],
            options={
                'ordering': ['created'],
                'verbose_name': 'contact',
                'verbose_name_plural': 'contacts',
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('text', models.TextField()),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contact.Contact')),
            ],
            options={
                'ordering': ['created'],
                'verbose_name': 'message',
                'verbose_name_plural': 'messages',
            },
        ),
    ]
