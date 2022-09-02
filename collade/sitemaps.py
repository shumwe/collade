from tutorials.models import Tutorial
from django.contrib.sitemaps import Sitemap

class TutorialSitemap(Sitemap):
    changefreq = 'daily'
    priority = 1
    
    def items(self):
        return Tutorial.objects.filter(publish=True)
    
    def lastmod(self, obj):
        return obj.updated
    
    def location(self, obj):
        return obj.get_absolute_url()