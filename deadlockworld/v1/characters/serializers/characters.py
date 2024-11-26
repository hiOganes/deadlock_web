# Standart libraries
# Other libraries
from rest_framework import serializers

# Project libraries
from v1.characters.models.characters import Characters


class CharactersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Characters
        fields = '__all__'