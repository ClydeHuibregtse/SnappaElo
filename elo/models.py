
from django.db import models
from django.db.models import F
import datetime

# Create your models here.
class RatingChange(models.Model):
    date = models.CharField(max_length=100)
    rating_at_time = models.IntegerField(default=1000)

class Player(models.Model):

    name = models.CharField(max_length=100)
    rating = models.IntegerField(default=1000)

    all_ratings = models.ManyToManyField(RatingChange)

    def __str__(self):
        return self.name + "-" + str(self.rating)

class Game(models.Model):

    # Django Fields
    score = models.CharField(max_length=10)
    players = models.ManyToManyField(Player, related_name="all_players")
    team1 = models.ManyToManyField(Player, related_name="team1")
    team2 = models.ManyToManyField(Player, related_name="team2")
    victors = models.IntegerField(default=0)
    note = models.CharField(max_length=200)

    def __str__(self):

        # player_objs = self.players.all()

        team1 = self.team1.all()
        team2 = self.team2.all()

        return team1[0].name + " and " + team1[1].name + " " + self.score.split('-')[0] + " - " + team2[0].name + " and " + team2[1].name + " " + self.score.split('-')[1]


    def calculate_new_ratings(self):

        # player_objs = self.players.all()
        #
        # player_ratings = [(player_objs[0].rating, player_objs[1].rating), (player_objs[2].rating, player_objs[3].rating)]

        team1 = self.team1.all()
        team2 = self.team2.all()

        o_1, o_2 = 0,0
        if self.victors == 0:
            o_1 = 1
        else:
            o_2 = 1

        # Calculate Win percentages
        E_1 = 1 / (1 + 10**(( sum(x.rating for x in team2)/2.0 - sum(x.rating for x in team1)/2.0)/400))
        E_2 = 1 - E_1

        # Update - this seems super janky - ask someone who knows SQL better to
        # help figure out why you can only update properly if you point directly
        # to the object and not iterate.
        player0 = team1[0]
        player1 = team1[1]
        player2 = team2[0]
        player3 = team2[1]

        player0.rating += 40 * (o_1 - E_1)
        rat0 = RatingChange(date=str(datetime.datetime.now()), rating_at_time=player0.rating)
        rat0.save()
        player0.all_ratings.add(rat0)
        player0.save()
        player1.rating += 40 * (o_1 - E_1)
        rat1 = RatingChange(date=str(datetime.datetime.now()), rating_at_time=player0.rating)
        rat1.save()
        player1.all_ratings.add(rat1)
        player1.save()
        player2.rating += 40 * (o_2 - E_2)
        rat2 = RatingChange(date=str(datetime.datetime.now()), rating_at_time=player0.rating)
        rat2.save()
        player2.all_ratings.add(rat2)
        player2.save()
        player3.rating += 40 * (o_2 - E_2)
        rat3 = RatingChange(date=str(datetime.datetime.now()), rating_at_time=player0.rating)
        rat3.save()
        player3.all_ratings.add(rat3)
        player3.save()
