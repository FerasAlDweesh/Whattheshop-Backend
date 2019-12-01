from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView
from .views import (
UserCreateAPIView,
DinosaurList,
OrderList,
OrderDetails
)


urlpatterns = [
    path('login/', TokenObtainPairView.as_view() , name='login'),
    path('register/', UserCreateAPIView.as_view(), name='register'),
    path('list/', DinosaurList.as_view(), name='list'),
    path('orders/', OrderList.as_view(), name='orders'),
    path('orders/<int:order_id>/', OrderDetails.as_view(), name='order-details')
]