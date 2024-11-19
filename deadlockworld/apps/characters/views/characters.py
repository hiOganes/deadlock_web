# Standart libraries
# Other libraries
from rest_framework.decorators import action
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.response import Response

# Project libraries
from apps.characters.models.characters import Characters
from apps.characters.models.spells import Spells
from apps.characters.serializers.characters import CharactersSerializer
from apps.characters.serializers.spells import SpellsSerializer


class CharactersViewSet(ReadOnlyModelViewSet):
    queryset = Characters.objects.all()
    serializer_class = CharactersSerializer

    @action(detail=True, methods=['get'])
    def character_spells(self, request, pk):
        spells = Spells.objects.filter(characters_id=pk)
        serializer = SpellsSerializer(spells, many=True)
        return Response(serializer.data)