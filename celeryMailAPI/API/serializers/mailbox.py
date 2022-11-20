from typing import Any, OrderedDict

from mailservice.models.mailbox import Mailbox
from rest_framework import serializers


class MailboxDefaultSerializer(serializers.ModelSerializer):
    last_update: serializers.ReadOnlyField = serializers.ReadOnlyField()
    sent: serializers.ReadOnlyField = serializers.ReadOnlyField()

    class Meta:
        model: Mailbox = Mailbox
        fields: list[str] = [
            "id",
            "host",
            "port",
            "login",
            "password",
            "email_from",
            "use_ssl",
            "is_active",
            "date",
            "last_update",
            "sent",
        ]

    def to_representation(self, instance) -> OrderedDict[Any, Any | None]:
        representation: OrderedDict[Any, Any | None] = super().to_representation(
            instance
        )
        representation["date"]: str = instance.date.strftime("%d-%m-%Y %H:%M:%S")
        representation["last_update"]: str = instance.last_update.strftime(
            "%d-%m-%Y %H:%M:%S"
        )
        return representation
