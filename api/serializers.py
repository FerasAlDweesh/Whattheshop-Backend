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

class OrderedItemSerializer(serializers.ModelSerializer):


    class Meta:
        model = OrderedItem
        fields = ['item', 'quantity']

        
        def get_quantity(self, obj):
            return obj.item.quantity

class OrderSerializer(serializers.ModelSerializer):


    ordered_item = OrderedItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ['customer', 'date', 'ordered_item', 'price' 'id']


