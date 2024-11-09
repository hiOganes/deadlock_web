# Standart libraries
# Other libraries
from django.db import models

# Project libraries
from .characters import Characters


class Spells(models.Model):
    title = models.CharField(max_length=255)
    description =models.TextField()
    cooldown = models.IntegerField()
    activity = models.BooleanField(default=False, blank=True)
    characters = models.ForeignKey(Characters, on_delete=models.CASCADE)
    image = models.ImageField(
        upload_to="characters/%Y/%m/%d/", 
        default=None, blank=True, 
        null=True
        )