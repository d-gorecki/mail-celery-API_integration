import uuid
from django.db import models


class Mailbox(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    host = models.CharField(max_length=320, help_text="SMTP server adress")
    port = models.IntegerField(default=465, help_text="connection port")
    login = models.CharField(max_length=32)
    password = models.CharField(max_length=32)
    email_from = models.CharField(max_length=32, help_text="sender name")
    use_ssl = models.BooleanField(default=True, help_text="SSL usage")
    is_active = models.BooleanField(default=False, help_text="mailbox status")
    date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(
        auto_now=True, help_text="value changes automatically during mailbox update"
    )
    sent = models.IntegerField(
        default=0, editable=False, help_text="number of messages sent from mailbox"
    )
