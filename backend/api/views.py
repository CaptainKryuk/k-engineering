from rest_framework import views, viewsets
from rest_framework.response import Response
from catalog.models import Material
from . import serializers


class CatalogViewSet(viewsets.ViewSet):

    def list(self, request):
        catalog = Material.objects.all()
        serializer = serializers.MaterialSerializer(catalog, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        return Response('success')



class SubscribeViewSet(viewsets.ViewSet):

    def create(self, request):
        serializer = serializers.SubscribeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)