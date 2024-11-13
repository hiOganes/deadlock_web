# Standart libraries
# Other libraries
from rest_framework import generics

# Project libraries
from apps.characters.models.characters import Characters
from apps.characters.serializers.character import CharacterSerializer


class CharacterAPIView(generics.ListAPIView):
    serializer_class = CharacterSerializer

    def get_queryset(self):
        return Characters.objects.filter(slug=self.kwargs['character_slug'])