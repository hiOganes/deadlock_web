# Other libraries
from django.urls import path, include
from rest_framework.routers import DefaultRouter

# Projects libraries
from apps.characters.views.characters import CharactersViewSet
from apps.characters.views.spells_list import SpellsAPIView


router = DefaultRouter()
router.register(r'characters', CharactersViewSet)


urlpatterns = router.urls