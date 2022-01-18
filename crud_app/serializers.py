from rest_framework import serializers
from .models import InventoryCollection, InventoryItem


class InventoryItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = InventoryItem
        fields = "__all__"


class InventoryCollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = InventoryCollection
        fields = "__all__"
