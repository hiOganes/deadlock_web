# Standart libraries
# Other libraries
from rest_framework.viewsets import ReadOnlyModelViewSet

# Project libraries
from v1.characters.models.spells import Spells
from v1.characters.serializers.spells import SpellsSerializer


class SpellsViewSet(ReadOnlyModelViewSet):
    queryset = Spells.objects.all()
    serializer_class = SpellsSerializer