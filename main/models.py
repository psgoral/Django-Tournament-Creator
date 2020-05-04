from django.db import models
from django.conf import settings



class Tournament(models.Model):

    typ_choices = [
        ('T', 'Tournament'),
        ('L', 'League'),

    ]

    name = models.CharField(max_length=100)
    number_of_players = models.IntegerField(default=0)
    typ = models.CharField(max_length=1,choices=typ_choices)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

class CheckIn(models.Model):
    player = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    tournament = models.ForeignKey(
        Tournament,
        on_delete=models.CASCADE)


class Match(models.Model):
    round_number = models.IntegerField()
    match_number = models.IntegerField()

    player1 = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="player1",
        null=True

    )

    player2 = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="player2",
        null=True
    )

    tournament = models.ForeignKey(
        Tournament,
        on_delete=models.CASCADE)

    score1 = models.IntegerField(
        null=True
    )
    score2 = models.IntegerField(
        null=True

    )

    score1byp1 = models.IntegerField(
    null=True
    )
    score1byp2 = models.IntegerField(
    null=True
    )

    score2byp1 = models.IntegerField(
    null=True
    )
    score2byp2 = models.IntegerField(
    null=True
    )

class Comment(models.Model):
    match = models.ForeignKey(
        Match,
        on_delete=models.CASCADE)

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE)
    
    message = Model.CharField(max_length=200)

    date = Model.DateTimeField(auto_now=True)


