# Standart libraries
# Other libraries
from django.contrib import admin

# Project impors
from apps.characters.models.characters import Characters
from apps.characters.models.spells import Spells


admin.site.register(Characters)