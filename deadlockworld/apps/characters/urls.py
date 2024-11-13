from django.urls import path

# Projects libraries
from apps.characters.views.characters_list import CharactersAPIView
from apps.characters.views.character_detail import CharacterAPIView
from apps.characters.views.spells_list import SpellsAPIView


urlpatterns = [
    path('characterslist/', CharactersAPIView.as_view()),
    path('spellslist/<int:character_id>/', SpellsAPIView.as_view()),
    path('character/<slug:character_slug>/', CharacterAPIView.as_view()),
]