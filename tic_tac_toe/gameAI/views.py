from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .game import TicTacToe
from .AI import AI
from .models import Tournament, Player, Game
from .serializers import TournamentSerializer, PlayerSerializer, GameSerializer






def start_game(player_1, player_2):
    """creates and return an empty tic_tac_toe"""
    if player_1 is None and player_2 is None:
        raise ValueError("Both players cannot be None")
    return Game.create(player_1 = player_1, player_2 = player_2) # create a emty game


def play(game, player, cell):
    if player not in [1, 2]:
        raise ValueError("Invalid player. Player must be 1 or 2.")
    if cell < 0 or cell > 8:
        raise ValueError("Invalid cell. Cell must be between 0 and 8.")
    # Make the player's move
    game.make_move(player, cell)
    # Check if the game is over
    if game.is_game_over():
        return game  # Game is over, no need for AI to play
    # Make AI's move
    game.make_ai_move()
    return game