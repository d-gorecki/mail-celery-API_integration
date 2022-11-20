from typing import Any

from django.utils.translation import gettext as _
from django_filters import rest_framework as filters
from django_filters.widgets import BooleanWidget
from mailservice.models.email import Email


class CustomBooleanWidget(BooleanWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.choices: tuple[tuple[str, Any], tuple[str, Any]] = (
            ("true", _("NOT sent")),
            ("false", _("Sent")),
        )


class EmailFilter(filters.FilterSet):
    CHOICES: tuple[tuple[bool, str]] = ((True, "NOT sent"), (False, "sent"))
    date: filters = filters.DateFilter(
        field_name="date",
        label="Created (YYYY-MM-DD or DD-MM-YYYY format)",
        input_formats=["%Y-%m-%d", "%d-%m-%Y"],
        lookup_expr="icontains",
    )
    sent_date: filters = filters.BooleanFilter(
        field_name="sent_date",
        label="Mail status",
        lookup_expr="isnull",
        widget=CustomBooleanWidget,
    )

    class Meta:
        model: Email = Email
        fields: list = []
