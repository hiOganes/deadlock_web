"""
URL configuration for deadlockworld project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.schemas import get_schema_view
from django.views.generic import TemplateView
from django.contrib.sitemaps.views import sitemap

# Projects libraries
from v1.characters.sitemaps import CharactersSitemap
from v1.shop.sitemaps import ShopSitemap
from v1.map.sitemaps import MapSitemap

sitemaps = {
    'characters': CharactersSitemap, 
    'shop': ShopSitemap,
    'map': MapSitemap,
    }

urlpatterns = [
    path(
        "sitemap.xml",
        sitemap,
        {"sitemaps": sitemaps},
        name="django.contrib.sitemaps.views.sitemap",
        ),
    path(
        "openapi/",
        get_schema_view(
            title="Your Project", 
            description="API for all things …", 
            version="1.0.0"
            ),
        name="api_schema",
        ),
    path(
        'swagger-ui/', 
        TemplateView.as_view(
            template_name='schema.html', 
            extra_context={'schema_url': 'api_schema'}
            ), 
        name='swagger-ui'
        ),
    path('admin/', admin.site.urls),
    path('api/v1/', include('v1.characters.urls')),
    path('api/v1/', include('v1.shop.urls')),
    path('api/v1/', include('v1.map.urls')),
]
