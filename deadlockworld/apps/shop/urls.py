from django.urls import path

# Projects libraries
from apps.shop.views.shop_list import ShopAPIView

urlpatterns = [
    path('shop_list/', ShopAPIView.as_view()),
]