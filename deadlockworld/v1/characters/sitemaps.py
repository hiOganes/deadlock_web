from django.contrib.sitemaps import Sitemap
from v1.characters.models.characters import Characters


class CharactersSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return Characters.objects.all()
    
    def lastmod(self, obj):
        return obj.update_date