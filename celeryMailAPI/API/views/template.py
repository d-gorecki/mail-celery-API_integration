from rest_framework import viewsets
from API.serializers.template import TemplateSerializer
from mailservice.models.template import Template


class TemplateViewSet(viewsets.ModelViewSet):
    queryset = Template.objects.all()
    serializer_class = TemplateSerializer
    http_method_names = ["get", "post", "put", "patch", "delete"]
