# Standart libraries
# Other libraries
from rest_framework import generics

# Project libraries
from apps.shop.models.shop import Shop
from apps.shop.serializers.shop import ShopSerializer


class ShopAPIView(generics.ListAPIView):
    serializer_class = ShopSerializer
    queryset = Shop.objects.all()