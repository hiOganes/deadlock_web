# Standart libraries
# Other libraries
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

# Project libraries
from v1.shop.models.shop import Shop
from v1.shop.serializers.shop import ShopSerializer


class ShopViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ShopSerializer
    queryset = Shop.objects.all()

    @action(detail=False)
    def weapon(self, request):
        items = Shop.objects.filter(category='weapon')
        serializer = ShopSerializer(items, many=True)
        return Response(serializer.data)

    @action(detail=False)
    def vitality(self, request):
        items = Shop.objects.filter(category='vitality')
        serializer = ShopSerializer(items, many=True)
        return Response(serializer.data)

    @action(detail=False)
    def spirit(self, request):
        items = Shop.objects.filter(category='spirit')
        serializer = ShopSerializer(items, many=True)
        return Response(serializer.data)

