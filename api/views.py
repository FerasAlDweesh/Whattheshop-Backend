from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView, DestroyAPIView
from .serializers import UserCreateSerializer, ListSerializer, OrderSerializer, CreateOrderSerializer
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import Dinosaur, Order, OrderedItem
from .permissions import IsOrderOwner
from rest_framework.permissions import IsAuthenticated
from datetime import datetime

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

class CreateOrderedItem(CreateAPIView):
	serializer_class = CreateOrderSerializer
	permission_classes = [IsAuthenticated]

	def perform_create(self, serializer):
		serializer.save(customer=self.request.user)
