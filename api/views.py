from rest_framework.generics import CreateAPIView, ListAPIView
from .serializers import UserCreateSerializer, ListSerializer
from .models import Dinosaur

class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer

class DinosaurList(ListAPIView):
	queryset = Dinosaur.objects.all()
	serializer_class = ListSerializer