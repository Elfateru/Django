from django.contrib.auth.models import Group
from rest_framework import serializers

from shopapp.models import Product, Order


class GroupSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = "pk", "name"


class ProductSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("pk",
                  "name",
                  "description",
                  "price",
                  "discount",
                  "created_at",
                  "archived",
                  "preview",
                  )


class OrderSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ("pk",
                  "delivery_address",
                  "promocode",
                  "created_at",
                  "user",
                  "products",
                  "receipt",
                  )
