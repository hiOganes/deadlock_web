from django.contrib import admin
from v1.map.models.map import Map
from v1.map.models.city import City


admin.site.register(Map)
admin.site.register(City)