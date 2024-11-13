# Standart libraries
# Other libraries
from rest_framework import generics

# Project libraries
from apps.characters.models.characters import Characters
from apps.characters.serializers.characters import CharactersSerializer

class CharactersAPIView(generics.ListAPIView):
    queryset = Characters.objects.all()
    serializer_class = CharactersSerializer