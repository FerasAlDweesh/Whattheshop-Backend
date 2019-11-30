from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView
from .views import (
UserCreateAPIView,
DinosaurList,
)


urlpatterns = [
    path('login/', TokenObtainPairView.as_view() , name='login'),
    path('register/', UserCreateAPIView.as_view(), name='register'),
    path('list/', DinosaurList.as_view(), name='list'),    
    path('profile/', views.Profile.as_view(), name="profile"),
]