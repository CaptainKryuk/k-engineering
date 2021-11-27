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
        collection = Material.objects.filter(collection__name=pk)
        serializer = serializers.MaterialSerializer(collection, many=True)
        return Response(serializer.data)


class MaterialViewSet(viewsets.ViewSet):

    def retrieve(self, request, pk=None):
        material = Material.objects.filter(item_number=pk).first()
        serializer = serializers.MaterialSerializer(material)
        return Response(serializer.data)


class OrderViewSet(viewsets.ViewSet):

    def create(self, request):
        serializer = serializers.OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class SubscribeViewSet(viewsets.ViewSet):

    def create(self, request):
        serializer = serializers.SubscribeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)