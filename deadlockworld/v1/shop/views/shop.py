# Standart libraries
# Other libraries
from rest_framework import viewsets, filters
from rest_framework.response import Response
from rest_framework.decorators import action

# Project libraries
from v1.shop.models.shop import Shop
from v1.shop.serializers.shop import ShopSerializer


class ShopView(viewsets.ReadOnlyModelViewSet):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']


    @action(detail=False)
    def weapon(self, request):
        if request.query_params.get('search', False):
            shop_items = Shop.objects.filter(
                title__icontains=request.query_params['search']
                )
        else:
            shop_items = Shop.objects.filter(category='weapon')
        serializer = ShopSerializer(shop_items, many=True)
        return Response(serializer.data)

    @action(detail=False)
    def vitality(self, request):
        shop_items = Shop.objects.filter(category='vitality')
        serializer = ShopSerializer(shop_items, many=True)
        return Response(serializer.data)

    @action(detail=False)
    def spirit(self, request):
        shop_items = Shop.objects.filter(category='spirit')
        serializer = ShopSerializer(shop_items, many=True)
        return Response(serializer.data)
    
    