from django.urls import path
from .views import tournament_detail, start_game, play_game

urlpatterns = [
    path('tournament/<int:tournament_id>/', tournament_detail, name='tournament-detail'),
    path('start_game/', start_game, name='start-game'),
    path('play_game/', play_game, name='play-game'),
]
