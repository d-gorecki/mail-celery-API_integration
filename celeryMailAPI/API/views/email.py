from API.filters import EmailFilter
from API.serializers.email import EmailSerializer
from django.db.models import QuerySet
from django_filters import rest_framework as filters
from mailservice.models.email import Email
from rest_framework import viewsets


class EmailViewSet(viewsets.ModelViewSet):
    serializer_class: EmailSerializer = EmailSerializer
    queryset: QuerySet[Email] = Email.objects.all()
    http_method_names: list[str] = ["get", "post"]
    filter_backends: tuple[filters] = (filters.DjangoFilterBackend,)
    filterset_class: EmailFilter = EmailFilter
