from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView, DestroyAPIView
from .serializers import UserCreateSerializer, ListSerializer, OrderSerializer
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
	queryset = Order.objects.all()
	serializer_class = OrderSerializer
	# permission_classes = [IsAuthenticated]

	def get_queryset(self):
		return Order.objects.filter(user=self.request.user, date__lte=datetime.today())

class OrderDetails(RetrieveAPIView):
	queryset = Order.objects.all()
	serializer_class = OrderSerializer
	# permission_classes = [IsAuthenticated]
	lookup_field = 'id'
	lookup_url_kwarg = 'order_id'

class CreateOrderedItem(CreateAPIView):
	serializer_class = OrderSerializer
	permission_classes = [IsAuthenticated]

	def perform_create(self, serializer):
		serializer.save(user=self.request.user, order_id=self.kwargs['order_id'])
