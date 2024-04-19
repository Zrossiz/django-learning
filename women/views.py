from rest_framework.response import Response
from rest_framework import generics
from .models import Women
from .serializers import WomenSerializer
from rest_framework.views import APIView


class WomenApiList(generics.ListCreateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer


class WomenApiDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
