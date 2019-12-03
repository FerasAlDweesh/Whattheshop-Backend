from django.contrib.auth.models import User
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView, DestroyAPIView
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated
from datetime import datetime
from .models import Dinosaur, Order, OrderedItem
from .serializers import UserCreateSerializer, ListSerializer, OrderSerializer, CreateOrderSerializer, ProfileSerializer
from .permissions import IsOrderOwner

class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer

class DinosaurList(ListAPIView):
	queryset = Dinosaur.objects.all()
	serializer_class = ListSerializer

class OrderList(ListAPIView):
	serializer_class = OrderSerializer
	permission_classes = [IsAuthenticated]

	def get_queryset(self):
		return Order.objects.filter(customer=self.request.user)

class OrderDetails(RetrieveAPIView):
	queryset = Order.objects.all()
	serializer_class = OrderSerializer
	permission_classes = [IsAuthenticated]
	lookup_field = 'id'
	lookup_url_kwarg = 'order_id'

class CreateOrder(CreateAPIView):
	serializer_class = CreateOrderSerializer
	permission_classes = [IsAuthenticated]

	def perform_create(self, serializer):
		serializer.save(customer=self.request.user)

class ProfileDetails(RetrieveAPIView):
	queryset = User.objects.all()
	serializer_class = ProfileSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'customer_id'

