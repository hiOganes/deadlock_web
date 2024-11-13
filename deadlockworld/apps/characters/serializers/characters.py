# Standart libraries
# Other libraries
from rest_framework import serializers

# Project libraries
from apps.characters.models.characters import Characters


class CharactersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Characters
        fields = ['image']