# Standart libraries
# Other libraries
from rest_framework import generics, filters

# Project libraries
from v1.shop.models.shop import Shop
from v1.shop.serializers.shop import ShopSerializer


class ShopView(generics.ListAPIView):
    serializer_class = ShopSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']
    
    def get_queryset(self):
        return Shop.objects.filter(category=self.kwargs['category'])