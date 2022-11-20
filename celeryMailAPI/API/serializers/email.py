from typing import Any, OrderedDict

from API.serializers.mailbox import MailboxDefaultSerializer
from API.serializers.template import TemplateSerializer
from mailservice.models import Mailbox
from mailservice.models.email import Email
from mailservice.tasks import send_email_task
from rest_framework import serializers, status
from rest_framework.exceptions import APIException


class CustomException(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = "Custom Exception Message"
    default_code = "invalid"

    def __init__(self, detail, status_code=None):
        self.detail = detail
        if status_code is not None:
            self.status_code = status_code


class EmailSerializer(serializers.ModelSerializer):
    sent_date: serializers.ReadOnlyField = serializers.ReadOnlyField()

    class Meta:
        model: Email = Email
        fields: list[str] = [
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

        representation["date"]: str = instance.date.strftime("%d-%m-%Y %H:%M:%S")
        if representation["sent_date"]:
            representation["sent_date"]: str = instance.sent_date.strftime(
                "%d-%m-%Y %H:%M:%S"
            )
        return representation

    def create(self, validated_data: dict[str, Any]) -> Email:
        """Overrides default create method in order to call send_email_task async method if mailbox.is_active.
        Always returns email model object."""
        mailbox: Mailbox = validated_data.get("mailbox")
        email: Email = Email(**validated_data)
        if mailbox.is_active:
            template_serialized: TemplateSerializer = TemplateSerializer(
                validated_data.get("template")
            )
            mailbox_serialized: MailboxDefaultSerializer = MailboxDefaultSerializer(
                mailbox
            )
            task_validated_data: dict[
                str, Any
            ] = (
                validated_data.copy()
            )  # copy of validated_data with model objects removed to be passed to celery task
            filename: str = validated_data.get("template").filename()
            task_validated_data.pop("template")
            task_validated_data.pop("mailbox")
            send_email_task.delay(
                mailbox_serialized.data,
                template_serialized.data,
                task_validated_data,
                filename,
                email.id,
            )
            email.save()
            return email
        else:
            raise CustomException(
                detail={"mailbox_status": "inactive"},
                status_code=status.HTTP_400_BAD_REQUEST,
            )
