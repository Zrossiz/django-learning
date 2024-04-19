from rest_framework.response import Response
from rest_framework import generics
from .models import Women
from .serializers import WomenSerializer
from rest_framework.views import APIView


class WomenApiList(generics.ListCreateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer

# class WomenApiView(APIView):
#     def get(self, request):
#         w = Women.objects.all()
#
#         return Response({'data': WomenSerializer(w, many=True).data})
#
#     def post(self, request):
#         serializer = WomenSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({'post': serializer.data})
#
#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get('pk', None)
#         if not pk:
#             return Response({'error': 'Method PUT not allowed'})
#         try:
#             instance = Women.objects.get(pk=pk)
#         except:
#             return Response({'error': 'Method PUT not allowed'})
#
#         serializer = WomenSerializer(data=request.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({"data": serializer.data})
#
#     def delete(self, request, *args, **kwargs):
#         pk = kwargs.get('pk', None)
#         if not pk:
#             return Response({"error": "Method DELETE not allowed"})
#
#         try:
#             instance = Women.objects.get(pk=pk)
#             instance.delete()
#         except:
#             return Response({"error": "Object not found"})
#
#         return Response({'Deleted item id': pk})