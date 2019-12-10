from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Dinosaur, Order, OrderedItem


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['username', 'password', 'first_name', 'last_name', 'email']

    def create(self, validated_data):
        username = validated_data['username']
        password = validated_data['password']
        first_name = validated_data['first_name']
        last_name = validated_data['last_name']
        email = validated_data['email']
        new_user = User(username=username, first_name=first_name, last_name=last_name, email=email)
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
    items = OrderedItemSerializer(many=True)
    class Meta:
        model = Order
        fields = ['customer', 'date', 'items', 'id']

    def get_customer(self, obj):
        return obj.customer.first_name

class CreateOrderedItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderedItem
        fields = ['item', 'quantity']

class CreateOrderSerializer(serializers.ModelSerializer):
    items = CreateOrderedItemSerializer(many=True)
    class Meta:
        model = Order
        fields = ['items']

    def create(self, validated_data):
        items = validated_data.pop('items')
        order = Order.objects.create(**validated_data)
        for item in items:
            OrderedItem.objects.create(**item, order=order)
        return order

class ProfileSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = ['username', 'name', 'email']

    def get_name(self, obj):
        return "%s %s"%(obj.first_name, obj.last_name)

    

