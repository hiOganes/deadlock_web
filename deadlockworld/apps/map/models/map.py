# Standart libraries
# Other libraries
from django.db import models

# Project libraries


class Map(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(
        upload_to="map/%Y/%m/%d/", 
        default=None, blank=True, 
        null=True
        )