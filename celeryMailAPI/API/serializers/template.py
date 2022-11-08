from typing import Any, OrderedDict
from rest_framework import serializers
from mailservice.models.template import Template
from datetime import datetime


class TemplateSerializer(serializers.ModelSerializer):
    last_update: serializers.ReadOnlyField = serializers.ReadOnlyField()

    class Meta:
        model: Template = Template
        fields: list[str] = [
            "id",
            "subject",
            "text",
            "attachment",
            "date",
            "last_update",
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
