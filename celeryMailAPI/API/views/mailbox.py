from rest_framework import viewsets
from API.serializers.mailbox import MailboxDefaultSerializer
from mailservice.models.mailbox import Mailbox


class MailboxViewSet(viewsets.ModelViewSet):
    queryset = Mailbox.objects.all()
    serializer_class = MailboxDefaultSerializer
    http_method_names = ["get", "post", "put", "patch", "delete"]
