from rest_framework import serializers
from store_app.models import (
    Item,
    ItemPack,
    ItemPackColor,
    Color,
    Order,
    OrderItem,
    Packaging,
    Users,
)


# For Converting models to json
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = "__all__"


class ItemSerializer(serializers.ModelSerializer):
    # img_url = serializers.FileField(use_url=True)

    class Meta:
        model = Item
        fields = ["id", "name", "description", "img_url"]


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = "__all__"


class PackagingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Packaging
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"


class ItemPackSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemPack
        fields = "__all__"


class ItemPackColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemPackColor
        fields = "__all__"


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = "__all__"
