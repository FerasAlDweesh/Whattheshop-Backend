from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Dinosaur, Order, OrderedItem


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['username', 'password']

    def create(self, validated_data):
        username = validated_data['username']
        password = validated_data['password']
        new_user = User(username=username)
        new_user.set_password(password)
        new_user.save()
        return validated_data

class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dinosaur
        fields = ['name', 'image', 'description', 'rarity', 'price', 'id']

class DinosaurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dinosaur
        fields = ['name', 'price']

class OrderedItemSerializer(serializers.ModelSerializer):
    item = DinosaurSerializer()
    class Meta:
        model = OrderedItem
        fields = ['item', 'quantity']

class OrderSerializer(serializers.ModelSerializer):
    customer = serializers.SerializerMethodField()
    ordereditem_set = OrderedItemSerializer(many=True)
    class Meta:
        model = Order
        fields = ['customer', 'date', 'ordereditem_set', 'id']

    def get_customer(self, obj):
        return obj.customer.first_name

class CreateOrderSerializer(serializers.ModelSerializer):
    # name = serializers.SerializerMethodField()
    # price = serializers.SerializerMethodField()
    class Meta:
        model = OrderedItem
        fields = ['item', 'quantity']

    # def get_name(self, obj):
    #     serializer = DinosaurSerializer()
    #     return serializer.name

    # def get_price(self, obj):
    #     serializer = DinosaurSerializer()
    #     return serializer.price
