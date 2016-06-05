# -*- coding: UTF-8 -*-

from __future__ import unicode_literals

import pytest
from mock import patch

from ..models import Contact


@pytest.mark.unit
@pytest.mark.django_db
class TestContact(object):
    """
    Contact unit test
    """

    @patch('pdepou.contact.models.Contact.objects.get', new=Contact)
    @patch('pdepou.contact.models.Contact.objects.create')
    def test_check_contact_existent(self, m_create):
        Contact.check_contact('Link', 'link@hirule.com')
        m_create.assert_not_called()
