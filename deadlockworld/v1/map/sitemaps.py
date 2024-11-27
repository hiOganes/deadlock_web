from django.contrib.sitemaps import Sitemap
from v1.map.models.map import Map


class MapSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return Map.objects.all()
    
    def lastmod(self, obj):
        return obj.update_date