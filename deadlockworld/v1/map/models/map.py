# Standart libraries
# Other libraries
from django.db import models
from django.shortcuts import reverse

# Project libraries


class Map(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    image = models.ImageField(
        upload_to="map/%Y/%m/%d/", 
        default=None, blank=True, 
        null=True
        )
    icons = models.ImageField(
        upload_to="map/%Y/%m/%d/", 
        default=None, blank=True, 
        null=True
        )
    

    def get_absolute_url(self):
        return reverse('map-detail', kwargs={'pk': self.pk})

# Map.objects.bulk_create([
#     Map(title='shrine', description="""patron shield""", image='map/image/2024/11/26/shrine.png', icons='map/icons/2024/11/13/shrine.png'),    
#     Map(title='crip1', description="""level 1 camp""", image='map/image/2024/11/26/crip.png', icons='map/icons/2024/11/13/crip1.png'),
#     Map(title='crip2', description="""level 2 camp""", image='map/image/2024/11/26/crip.png', icons='map/icons/2024/11/13/crip2.png'),
#     Map(title='crip3', description="""level 3 camp""", image='map/image/2024/11/26/crip.png', icons='map/icons/2024/11/13/crip3.png'),
#     Map(title='guardian', description="""first tower""", image='map/image/2024/11/26/guardian.png', icons='map/icons/2024/11/13/guardian.png'),
#     Map(title='patron', description="""final tower""", image='map/image/2024/11/26/patron.png', icons='map/icons/2024/11/13/patron.png'),
#     Map(title='guardians', description="""third tower""", image='map/image/2024/11/26/guardians.png', icons='map/icons/2024/11/13/guardian.png'),
#     Map(title='shop', description="""the curiosity shop""", image='map/image/2024/11/26/shop.png', icons='map/icons/2024/11/13/shop.png'),
#     Map(title='slot machine', description="""slot machine""", image='map/image/2024/11/26/slot_machine.png', icons='map/icons/2024/11/13/slot_machine.png'),
#     Map(title='urn', description="""urn with souls""", image='map/image/2024/11/26/urn.png', icons='map/icons/2024/11/13/urn.png'),
#     Map(title='walker.png', description="""second tower""", image='map/image/2024/11/26/walker.png', icons='map/icons/2024/11/13/walker.png')
# ])