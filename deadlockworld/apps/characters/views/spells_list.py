# Standart libraries
# Other libraries
from rest_framework import generics

# Project libraries
from apps.characters.models.spells import Spells
from apps.characters.serializers.spells import SpellsSerializer


class SpellsAPIView(generics.ListAPIView):
    serializer_class = SpellsSerializer

    def get_queryset(self):
        return Spells.objects.filter(characters_id=self.kwargs['character_id'])