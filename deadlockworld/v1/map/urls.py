# Standart libraries
# Other libraries
from django.urls import path
from rest_framework.routers import DefaultRouter

# Project libraries
from v1.map.views.map import MapViewSet
from v1.map.views.city import CityView

router = DefaultRouter()
router.register(r'map', MapViewSet)
router.register(r'city', CityView)