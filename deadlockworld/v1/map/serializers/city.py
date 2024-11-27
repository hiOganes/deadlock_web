# Standart libraries
# Other libraries
from rest_framework import serializers

# Project libraries
from v1.map.models.city import City


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'