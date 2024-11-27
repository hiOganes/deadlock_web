from django.contrib import admin
from v1.characters.models.characters import Characters
from v1.characters.models.spells import Spells


admin.site.register(Characters)
admin.site.register(Spells)
