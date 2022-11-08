from django.urls import reverse

from API.tests import factory as api_factory
from rest_framework.test import APITestCase
from API.serializers.mailbox import MailboxDefaultSerializer
from API.serializers.email import EmailSerializer
from rest_framework import status
from mailservice.models.template import Template
from mailservice.models.mailbox import Mailbox
from mailservice.models.email import Email


class TestAPI(APITestCase):
    def setUp(self) -> None:
        pass

    def test_create_template(self):
        response = self.client.post(
            reverse("template-list"), {"subject": "test", "text": "test"}
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Template.objects.count(), 1)

    def test_create_mailbox(self):
        mailbox_dict = MailboxDefaultSerializer(api_factory.MailboxFactory).data
        response = self.client.post(reverse("mailbox-list"), mailbox_dict)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Mailbox.objects.count(), 1)

    def test_create_email(self):
        template = api_factory.TemplateFactory()
        mailbox = api_factory.MailboxFactory()
        email_dict = {
            "mailbox": f"{mailbox.id}",
            "template": f"{template.id}",
            "to": ["test@gmail.com"],
            "reply_to": "test@gmail.com",
        }
        response = self.client.post(reverse("email-list"), email_dict)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Email.objects.count(), 1)

    def test_send_email_from_not_active_mailbox(self):
        email = api_factory.EmailFactory()
