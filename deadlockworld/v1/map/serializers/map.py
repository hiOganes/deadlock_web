# Standart libraries
# Other libraries
from rest_framework import serializers

# Project libraries
from v1.map.models.map import Map


class MapSerializer(serializers.ModelSerializer):
    class Meta:
        model = Map
        fields = '__all__'