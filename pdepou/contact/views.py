# -*- coding: UTF-8 -*-

from __future__ import unicode_literals, absolute_import

from braces.views import AjaxResponseMixin

from django.views.generic import View
from django.http import HttpResponse

from pdepou.core.utils import send_email

from .models import Contact, Message


class ContactView(AjaxResponseMixin, View):
    """
    Contact Class Based View
    """

    def post_ajax(self, request, *args, **kwargs):
        """
        HTTP POST request that registers a contact
        """
        name = request.POST.get('name')
        email = request.POST.get('email')
        text = request.POST.get('text')
        contact = Contact.check_contact(name=name, email=email)
        Message.objects.create(text=text, contact=contact)
        send_email('Mensaje directo de {}'.format(name), text)
        return HttpResponse()
