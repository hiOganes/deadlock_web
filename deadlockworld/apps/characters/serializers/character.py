# Standart libraries
# Other libraries
from rest_framework import serializers

# Project libraries
from apps.characters.models.characters import Characters


class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Characters
        fields = [
            'image',
            'story',
            'dps',
            'bullet_damage',
            'bullet_per_second',
            'ammo',
            'light_melee',
            'heavy_melee',
            'max_health',
            'health_regen',
            'stamina',
            'move_speed',
            'sprint_speed',
            'bullet_resist',
            'spirit_resist',
        ]