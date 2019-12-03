from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView
from .views import (
UserCreateAPIView,
DinosaurList,
OrderList,
OrderDetails,
CreateOrderedItem,
DinosaurList, 
ProfileDetails,
)


urlpatterns = [
    path('login/', TokenObtainPairView.as_view() , name='login'),
    path('register/', UserCreateAPIView.as_view(), name='register'),
  
    path('dinosaurs/', DinosaurList.as_view(), name='dinosaur-list'),
    path('orders/create/', CreateOrderedItem.as_view(), name='create-order'),
    path('orders/', OrderList.as_view(), name='orders'),
    path('orders/<int:order_id>/', OrderDetails.as_view(), name='order-details'),
 
    path('profile/<int:customer_id>/', ProfileDetails.as_view(), name="profile"),
]