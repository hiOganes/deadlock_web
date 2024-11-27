from django.contrib.sitemaps import Sitemap
from v1.shop.models.shop import Shop


class ShopSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return Shop.objects.all()
    
    def lastmod(self, obj):
        return obj.update_date