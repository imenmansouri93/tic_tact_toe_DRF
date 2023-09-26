from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .game import TicTacToe
from .AI import AI
from .models import Tournament, Player, Game
from .serializers import TournamentSerializer, PlayerSerializer, GameSerializer


@api_view(['GET'])
def tournament_detail(request, tournament_id):
    tournament = Tournament.objects.get(pk=tournament_id)
    serializer = TournamentSerializer(tournament)
    return Response(serializer.data)


@api_view(['POST'])
def start_game(request):
    # Initialize the game, AI, and played_moves here
    ai = AI()
    game = TicTacToe(ai)
    played_moves = set()

    if request.method == "POST":
        # Reset button, reset the game
        game.reset_game()
        initial_game_data = game.get_board()
        played_moves.clear()

        # AI makes the first move
        game.play(None)
        initial_game_data = game.get_board()
        for move in game.get_AI_last_played_move():
            played_moves.add(move)

        return Response({"game_data": initial_game_data}, status=status.HTTP_200_OK)

    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['POST'])
def play_game(request):
    # Initialize the game, AI, and played_moves here
    ai = AI()
    game = TicTacToe(ai)
    played_moves = set()

    if request.method == "POST":
        if "cell_value" in request.data:
            # User clicked a cell button, process the move and update game state
            cell_value = request.data.get("cell_value")
            if cell_value not in played_moves:
                played_moves.add(cell_value)
                game.play(cell_value)

                # AI move
                game.play(None)
                for move in game.get_AI_last_played_move():
                    played_moves.add(move)
                updated_game_data = game.get_board()

                return Response({"game_data": updated_game_data}, status=status.HTTP_200_OK)

    return Response(status=status.HTTP_204_NO_CONTENT)