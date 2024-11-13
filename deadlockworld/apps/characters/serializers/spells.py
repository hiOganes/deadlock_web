# Standart libraries
# Other libraries
from rest_framework import serializers

# Project libraries
from apps.characters.models.spells import Spells

class SpellsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Spells
        fields = [
            'title', 
            'description', 
            'description_image', 
            'cooldown', 
            'image',
            ]