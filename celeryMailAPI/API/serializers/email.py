from typing import OrderedDict, Any
from rest_framework import serializers
from mailservice.models.email import Email
from mailservice.tasks import send_email_task


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
        representation["last_update"] = instance.last_update.strftime(
            "%d-%m-%Y %H:%M:%S"
        )
        return representation

    def create(self, validated_data):
        mailbox = validated_data.get("mailbox")
        if mailbox.is_active:
            send_email_task(mailbox, validated_data.get("template"), validated_data)
        return Email.obects.create(**validated_data)
