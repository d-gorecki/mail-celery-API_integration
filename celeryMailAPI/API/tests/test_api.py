from API.serializers.mailbox import MailboxDefaultSerializer
from API.tests import factory as api_factory
from django.urls import reverse
from mailservice.models.email import Email
from mailservice.models.mailbox import Mailbox
from mailservice.models.template import Template
from rest_framework import status
from rest_framework.test import APITestCase


class TestAPI(APITestCase):
    def test_create_template(self):
        response = self.client.post(
            reverse("template-list"), {"subject": "test", "text": "test"}
        )
        self.assertEqual(
            response.status_code, status.HTTP_201_CREATED, f"{response.data}"
        )
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
        mailbox = api_factory.MailboxFactory()
        mailbox.is_active = False
        mailbox.save()
        template = api_factory.TemplateFactory()
        email_dict = {
            "mailbox": f"{mailbox.id}",
            "template": f"{template.id}",
            "to": ["test@gmail.com"],
            "reply_to": "test@gmail.com",
        }
        response = self.client.post(reverse("email-list"), email_dict)
        self.assertEqual(
            response.status_code, status.HTTP_400_BAD_REQUEST, f"{response.data}"
        )

    def test_delete_mailbox(self):
        mailbox = api_factory.MailboxFactory()
        response = self.client.delete(
            reverse("mailbox-detail", kwargs={"pk": mailbox.id})
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Mailbox.objects.count(), 0)

    def test_patch_mailbox(self):
        mailbox = api_factory.MailboxFactory()
        response = self.client.patch(
            reverse("mailbox-detail", kwargs={"pk": mailbox.id}), {"host": "patched"}
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Mailbox.objects.get(pk=mailbox.pk).host, "patched")
