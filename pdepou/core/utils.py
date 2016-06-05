# -*- coding: UTF-8 -*-

from __future__ import unicode_literals, absolute_import

from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.conf import settings


def send_email(subject, text):
    """
    Function that sends me an email to notify something
    TODO: If some day I have a dedicated server put this function
          in a Celery asynchronous task
    :param subject: Email subject
    :param text: Email text
    """
    msg = EmailMultiAlternatives(subject=subject,
                                 from_email=settings.DEFAULT_EMAIL,
                                 to=[settings.DEFAULT_EMAIL])
    msg.attach_alternative(render_to_string(
        'contact/emails/_email_contacto.html',
        {'body_email': text}), 'text/html')
    msg.send()
