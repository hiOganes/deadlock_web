# Other libraries
from django.urls import path, include
from rest_framework.routers import DefaultRouter

# Projects libraries
from apps.characters.views.characters import CharactersViewSet
from apps.characters.views.spells import SpellsViewSet


router = DefaultRouter()
router.register(r'characters', CharactersViewSet, basename='characters')
router.register(r'spells', SpellsViewSet, basename='spells')


urlpatterns = router.urls