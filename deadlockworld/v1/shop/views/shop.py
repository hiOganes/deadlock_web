# Standart libraries
# Other libraries
from rest_framework import generics

# Project libraries
from v1.shop.models.shop import Shop
from v1.shop.serializers.shop import ShopSerializer


class ShopView(generics.ListAPIView):
    serializer_class = ShopSerializer
    
    def get_queryset(self):
        return Shop.objects.filter(category=self.kwargs['category'])