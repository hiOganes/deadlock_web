from django.urls import path
from rest_framework import routers

# Projects libraries
from apps.shop.views.shop import ShopViewSet


router = routers.DefaultRouter()
router.register(r'shop', ShopViewSet)


urlpatterns = router.urls