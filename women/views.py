from rest_framework import viewsets

from women.models import Women
from women.serializers import WomenSerializer


class WomenViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
