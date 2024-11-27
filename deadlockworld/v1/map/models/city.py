from django.db import models


class City(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(
        upload_to='map/%Y/%m/%d',
        blank=True,
        default=None,
        null=True,
        )
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True)
 
    class Meta:
        verbose_name_plural = 'City'

# City.objects.bulk_create([
#     City(title='crowleys', image='map/images_city/2024/11/26/crowleys.png', slug='crowleys'),        
#     City(title='dark_street', image='map/images_city/2024/11/26/dark_street.png', slug='dark_street'),
#     City(title='records', image='map/images_city/2024/11/26/records.png', slug='records'),
#     City(title='station', image='map/images_city/2024/11/26/station.png', slug='station'),
#     City(title='table', image='map/images_city/2024/11/26/table.png', slug='table')        
# ])