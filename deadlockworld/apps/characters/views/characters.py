# Standart libraries
# Other libraries
from rest_framework import generics
from rest_framework.viewsets import ReadOnlyModelViewSet

# Project libraries
from apps.characters.models.characters import Characters
from apps.characters.serializers.characters import CharactersSerializer


class CharactersViewSet(ReadOnlyModelViewSet):
    queryset = Characters.objects.all()
    serializer_class = CharactersSerializer