from django.urls import path
from rest_framework import routers

# Projects libraries
from v1.shop.views.shop import ShopView


# router = routers.DefaultRouter()
# router.register(r'shop', ShopViewSet)


# urlpatterns = router.urls


urlpatterns = [
    path('shop/<slug:category>/', ShopView.as_view(), name='shop'),
]