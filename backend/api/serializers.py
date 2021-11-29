from rest_framework import serializers, viewsets
from rest_framework.fields import SerializerMethodField
from catalog.models import Material
from subscribes.models import Subscribe
from orders.models import Order

class MaterialSerializer(serializers.ModelSerializer):
    quantity = SerializerMethodField()

    class Meta:
        model = Material
        fields = '__all__'
        depth = 2

    
    def get_quantity(self, instance):
        if instance.quantity > 1:
            return 'many'
        elif instance.quantity > 0 and instance.quantity <= 1:
            return 'not_many'
        else:
            return 'empty'


class SubscribeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subscribe
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = '__all__'
