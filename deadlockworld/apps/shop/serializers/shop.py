# Standart libraries
# Other libraries
from rest_framework import serializers

# Project libraries
from apps.shop.models.shop import Shop


class ShopSerializer(serializers.ModelSerializer):
    class Meta:
       model = Shop
       fields = '__all__'