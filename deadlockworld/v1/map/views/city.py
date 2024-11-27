# Standart libraries
# Other libraries
from rest_framework import generics

# Project libraries
from v1.map.models.city import City
from v1.map.serializers.city import CitySerializer

class CityView(generics.ListAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer