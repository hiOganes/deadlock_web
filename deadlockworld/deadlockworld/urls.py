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
from rest_framework.routers import DefaultRouter
from django.views.generic import TemplateView
from django.contrib.sitemaps.views import sitemap

# Projects libraries
from deadlockworld.sitemaps import sitemaps
from v1.characters.urls import router as v1_characters_and_spells_router
from v1.map.urls import router as v1_map_and_city_router
from v1.shop.urls import router as v1_shop_router


v1_router = DefaultRouter()
v1_router.registry.extend(v1_characters_and_spells_router.registry)
v1_router.registry.extend(v1_map_and_city_router.registry)
v1_router.registry.extend(v1_shop_router.registry)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/v1/', include((v1_router.urls, 'api'), namespace='v1')),

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
]
