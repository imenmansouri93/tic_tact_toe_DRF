# models.py

from django.db import models



class Tournament(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Player(models.Model):
    name = models.CharField(max_length=255)
    python_code = models.TextField()

    def __str__(self):
        return self.name

class Game(models.Model):
    tournament_id = models.ForeignKey('Tournament', null=True, on_delete=models.SET_NULL)
    player_1 = models.ForeignKey('Player', related_name='player_1_games', on_delete=models.CASCADE)
    player_2 = models.ForeignKey('Player', related_name='player_2_games', on_delete=models.CASCADE)
    moves = models.JSONField(default=list)
    winner = models.PositiveSmallIntegerField(choices=[(1, 'Player 1'), (2, 'Player 2')], null=True)

    def __str__(self):
        return f"Game #{self.id}"









