# Standart libraries
# Other libraries
from rest_framework.viewsets import ReadOnlyModelViewSet

# Project libraries
from v1.map.models.map import Map
from v1.map.serializers.map import MapSerializer

class MapViewSet(ReadOnlyModelViewSet):
    queryset = Map.objects.all()
    serializer_class = MapSerializer