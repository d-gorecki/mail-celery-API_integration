from typing import Any, OrderedDict
from rest_framework import serializers
from mailservice.models.template import Template


class TemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Template
        fields = ["id", "subject", "text", "attachment", "date", "last_update"]

    def to_representation(self, instance) -> OrderedDict[Any, Any | None]:
        representation: OrderedDict[Any, Any | None] = super().to_representation(
            instance
        )
        representation["date"] = instance.date.strftime("%d-%m-%Y %H:%M:%S")
        representation["last_update"] = instance.last_update.strftime(
            "%d-%m-%Y %H:%M:%S"
        )
        return representation
