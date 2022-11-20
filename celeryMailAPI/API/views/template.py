from API.serializers.template import TemplateSerializer
from django.db.models import QuerySet
from mailservice.models.template import Template
from rest_framework import viewsets


class TemplateViewSet(viewsets.ModelViewSet):
    queryset: QuerySet[Template] = Template.objects.all()
    serializer_class: TemplateSerializer = TemplateSerializer
    http_method_names: list[str] = ["get", "post", "put", "patch", "delete"]
