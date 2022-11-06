from rest_framework import viewsets
from mailservice.models.email import Email
from API.serializers.email import EmailSerializer


class EmailViewSet(viewsets.ModelViewSet):
    serializer_class = EmailSerializer
    queryset = Email.objects.all()
    http_method_names = ["get", "post"]
