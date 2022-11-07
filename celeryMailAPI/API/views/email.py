from rest_framework import viewsets
from mailservice.models.email import Email
from API.serializers.email import EmailSerializer
from django_filters import rest_framework as filters
from API.filters import EmailFilter


class EmailViewSet(viewsets.ModelViewSet):
    serializer_class = EmailSerializer
    queryset = Email.objects.all()
    http_method_names = ["get", "post"]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = EmailFilter
