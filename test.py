from elo.models import Player, Game
import random

players = [Player(name="Clyde"), Player(name="Gabe"), Player(name="Johnny"), Player(name="JX")]
for player in players:
    player.save()

scores = ["7-5",
          "5-6",
          "7-8",
          "7-6",
          "7-3",
          "4-5",
          "5-5",
          "3-5",
          "2-5",
          "2-5",
          "2-5",
          "7-5",
          "7-5",
          "7-5",
          "7-5",
          "7-5",
          "7-5",
          "7-5",
          "7-5",
          "7-5",
          "7-5",
          "7-5",
          ]

games = []
for score in scores:
    new_game = Game(score=score)
    new_game.victors = 1 if random.random() > .5 else 0
    new_game.save()

    i = 0
    for player in players:
        if i in [0,1]:
            new_game.team1.add(player)
        else:
            new_game.team2.add(player)

        i += 1
        new_game.players.add(player)
    new_game.save()
    games.append(new_game)



for game in games:
    game.calculate_new_ratings()

# game1 = Game(score="7-5")
# game1.victors = 1
# game1.save()

# for player in players:
#     player.save()
#
#     game1.players.add(player)
#     game1.save()
# print(game1)
# game1.calculate_new_ratings()
# game1.save()
