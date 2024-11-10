# Standart libraries
# Other libraries
from django.db import models

# Project libraries


class Shop(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.IntegerField()
    image = models.ImageField(
        upload_to="shop/%Y/%m/%d/", 
        default=None, blank=True, 
        null=True
        )
    category = models.CharField(max_length=255)
    activity = models.BooleanField(default=False, blank=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    slug = models.CharField(max_length=255)

    class Meta:
        ordering = ['price']
        indexes = [models.Index(fields=['price'])]