from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import redirect
from django.contrib.sitemaps import GenericSitemap
from django.contrib.sitemaps.views import sitemap
from collade.sitemaps import TutorialSitemap

sitemaps = {
    'tutorial': TutorialSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('accounts/', include('accounts.urls')),
    path('core/', include('core.urls')),
    path('tutorials/', include('tutorials.urls')),
    path('', lambda req: redirect('tutorials')),
    path('sitemaps.xml', sitemap, {
        'sitemaps':sitemaps
        }, name='collade_sitemaps'),
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = "COLLADE"
admin.site.site_title = "COLLADE"
admin.site.index_title = 'Welcome :)'