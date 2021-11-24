from rest_framework import serializers, viewsets
from catalog.models import Material
from subscribes.models import Subscribe

class MaterialSerializer(serializers.ModelSerializer):

    class Meta:
        model = Material
        fields = '__all__'
        depth = 2


class SubscribeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subscribe
        fields = '__all__'
