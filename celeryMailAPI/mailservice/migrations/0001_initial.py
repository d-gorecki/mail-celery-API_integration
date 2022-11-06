# Generated by Django 4.1.3 on 2022-11-06 14:10

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Mailbox",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "host",
                    models.CharField(help_text="SMTP server adress", max_length=320),
                ),
                ("port", models.IntegerField(default=465, help_text="connection port")),
                ("login", models.CharField(max_length=32)),
                ("password", models.CharField(max_length=32)),
                (
                    "email_from",
                    models.CharField(help_text="sender name", max_length=32),
                ),
                ("use_ssl", models.BooleanField(default=True, help_text="SSL usage")),
                (
                    "is_active",
                    models.BooleanField(default=False, help_text="mailbox status"),
                ),
                ("date", models.DateTimeField(auto_now_add=True)),
                (
                    "last_update",
                    models.DateTimeField(
                        auto_now=True,
                        help_text="value changes automatically during mailbox update",
                    ),
                ),
                (
                    "sent",
                    models.IntegerField(
                        help_text="number of messages sent from mailbox"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Template",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "subject",
                    models.CharField(help_text="message subject", max_length=64),
                ),
                ("text", models.TextField(help_text="message text")),
                ("attachment", models.FileField(upload_to="")),
                ("date", models.DateTimeField(auto_now_add=True)),
                (
                    "last_update",
                    models.DateTimeField(
                        auto_now=True,
                        help_text="value changes automatically during template update",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Email",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "to",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.EmailField(max_length=254),
                        help_text="receivers",
                        size=None,
                    ),
                ),
                (
                    "cc",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.EmailField(max_length=254),
                        help_text="copy receivers",
                        null=True,
                        size=None,
                    ),
                ),
                (
                    "bcc",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.EmailField(max_length=254),
                        help_text="hidden copy receivers",
                        null=True,
                        size=None,
                    ),
                ),
                (
                    "reply_to",
                    models.EmailField(
                        default=None, help_text="reply mail", max_length=254, null=True
                    ),
                ),
                ("sent_date", models.DateTimeField(auto_now_add=True)),
                (
                    "mailbox",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="mailservice.mailbox",
                    ),
                ),
                (
                    "template",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="mailservice.template",
                    ),
                ),
            ],
        ),
    ]