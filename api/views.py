from rest_framework.generics import CreateAPIView, ListAPIView
from .serializers import UserCreateSerializer, ListSerializer
from .models import Dinosaur

class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer

class DinosaurList(ListAPIView):
	queryset = Dinosaur.objects.all()
	serializer_class = ListSerializer

class ProfileDetails(RetrieveAPIView):
	serializer_class = ProfileSerializer

	def get_object(self):
		return self.request.user.profile