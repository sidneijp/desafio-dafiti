from rest_framework import serializers

from .models import Shoe


class ShoeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shoe
        fields = ['id', 'sku', 'name', 'color', 'stock', 'price']


class ShoeCsvSerializer(serializers.Serializer):
    file = serializers.FileField(use_url=False)
