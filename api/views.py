from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView, destroyAPIView
from .serializers import UserCreateSerializer, ListSerializer, DetailSerializer
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import Dinosaur, Order, OrderedItem
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
		return Order.objects.filter(user=self.request.user, date__gte=datetime.today())

class CreateOrder(CreateAPIView):
	serializer_class = OrderSerializer
	permission_classes = [IsAuthenticated]

	def perform_create(self, serializer):
		serializer.save(user=self.request.user, order_id=self.kwargs['order_id'])

class DeleteOrder(destroyAPIView):
	queryset = Order.objects.all()
	lookup_field = 'id'
	lookup_url_kwarg = 'order_id'
	permission_classes = [IsAuthenticated, IsBookingOwner, IsStaff]
