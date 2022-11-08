from django.db.models import QuerySet
from rest_framework import viewsets
from API.serializers.mailbox import MailboxDefaultSerializer
from mailservice.models.mailbox import Mailbox


class MailboxViewSet(viewsets.ModelViewSet):
    queryset: QuerySet[Mailbox] = Mailbox.objects.all()
    serializer_class: MailboxDefaultSerializer = MailboxDefaultSerializer
    http_method_names: list[str] = ["get", "post", "put", "patch", "delete"]
