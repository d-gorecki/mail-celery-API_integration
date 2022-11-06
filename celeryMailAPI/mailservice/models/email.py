import uuid
from django.db import models
from .mailbox import Mailbox
from .template import Template
from django.contrib.postgres.fields import ArrayField


class Email(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    mailbox = models.ForeignKey(Mailbox, on_delete=models.CASCADE)
    template = models.ForeignKey(Template, on_delete=models.CASCADE)
    to = ArrayField(models.EmailField(), help_text="receivers")
    cc = ArrayField(models.EmailField(), help_text="copy receivers", null=True)
    bcc = ArrayField(models.EmailField(), help_text="hidden copy receivers", null=True)
    reply_to = models.EmailField(default=None, null=True, help_text="reply mail")
    date = models.DateField(auto_now=True, help_text="Creation date")
    sent_date = models.DateTimeField(
        default=None,
        null=True,
        editable=False,
        help_text="set after successful mail send",
    )
