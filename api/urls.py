from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView
from .views import (
UserCreateAPIView,
DinosaurList, ProfileDetails
)


urlpatterns = [
    path('login/', TokenObtainPairView.as_view() , name='login'),
    path('register/', UserCreateAPIView.as_view(), name='register'),
    path('list/', DinosaurList.as_view(), name='list'),    
    path('profile/<int:customer_id>/', ProfileDetails.as_view(), name="profile"),
]