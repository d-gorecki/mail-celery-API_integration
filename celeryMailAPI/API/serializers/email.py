from typing import OrderedDict, Any
from rest_framework import serializers
from mailservice.models.email import Email
from mailservice.tasks import send_email_task
from API.serializers.template import TemplateSerializer
from API.serializers.mailbox import MailboxDefaultSerializer


class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Email
        fields = [
            "id",
            "mailbox",
            "template",
            "to",
            "cc",
            "bcc",
            "reply_to",
            "date",
            "sent_date",
        ]

    def to_representation(self, instance) -> OrderedDict[Any, Any | None]:
        representation: OrderedDict[Any, Any | None] = super().to_representation(
            instance
        )
        representation["date"] = instance.date.strftime("%d-%m-%Y %H:%M:%S")
        if representation["sent_date"]:
            representation["sent_date"] = instance.sent_date.strftime(
                "%d-%m-%Y %H:%M:%S"
            )
        return representation

    def create(self, validated_data):
        mailbox = validated_data.get("mailbox")
        if mailbox.is_active:
            template_serialized = TemplateSerializer(validated_data.get("template"))
            mailbox_serialized = MailboxDefaultSerializer(mailbox)
            task_validated_data = (
                validated_data.copy()
            )  # copy of validated_data with model objects removed to be pased to celery task
            filename = validated_data.get("template").filename()
            task_validated_data.pop("template")
            task_validated_data.pop("mailbox")
            send_email_task.delay(
                mailbox_serialized.data,
                template_serialized.data,
                task_validated_data,
                filename,
            )
        return Email.objects.create(**validated_data)
