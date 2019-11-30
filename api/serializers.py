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

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['customer', 'date', 'item', 'id']

class OrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['item', 'quantity', 'price', 'date', 'id']
