# Standart libraries
# Other libraries
from rest_framework import viewsets

# Project libraries
from v1.shop.models.shop import Shop
from v1.shop.serializers.shop import ShopSerializer


class ShopViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ShopSerializer
    queryset = Shop.objects.all()