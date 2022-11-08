import os.path
import uuid
from typing import Optional

from django.db import models
from django.conf import settings


class Template(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    subject = models.CharField(max_length=64, help_text="message subject")
    text = models.TextField(help_text="message text")
    attachment = models.FileField(upload_to="", null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(
        auto_now=True, help_text="value changes automatically during template update"
    )

    def filename(self) -> Optional[str]:
        if self.attachment:
            return os.path.join(settings.MEDIA_ROOT, self.attachment.name)
