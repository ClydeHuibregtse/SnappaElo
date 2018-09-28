from django.shortcuts import render
from elo.models import Player, Game
from django.template import loader
# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from .forms import GameForm

from django.contrib.auth.decorators import login_required


def index(request):
    template = loader.get_template('elo/index.html')
    if request.method == 'POST':
        form = GameForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data

            players = (data["player0"], data["player1"], data["player2"], data["player3"])
            score = str(data["score0"]) + "-" + str(data["score1"])
            new_game = Game(score=score)
            new_game.save()
            new_game.victors = 0 if int(score.split('-')[0]) > int(score.split('-')[1]) else 1

            i = 0
            for player in players:

                player_obj = Player.objects.get(name=player.split('-')[0])

                if i in [0,1]:
                    new_game.team1.add(player_obj)
                else:
                    new_game.team2.add(player_obj)

                new_game.players.add(player_obj)

                i += 1

            new_game.save()

            new_game.calculate_new_ratings()

            return HttpResponseRedirect('success_game/')
    else:
        form = GameForm()

    context = {'all_players': sorted(Player.objects.all(), key=lambda x: -x.rating),
               'form': form}

    return HttpResponse(template.render(context, request))


def succ_game(request):
    template = loader.get_template('elo/success_game.html')
    context = {'game': list(Game.objects.all())[-1]}
    return HttpResponse(template.render(context, request))


def player_view(request, player_name):
    template = loader.get_template('elo/ind_player.html')
    player = Player.objects.get(name=player_name)

    datax = [str(x.date) for x in player.all_ratings.all()]
    datay = [y.rating_at_time for y in player.all_ratings.all()]

    wins_dict = dict()
    loss_dict = dict()

    for game in Game.objects.all():
        players = list(game.players.all())
        team1 = set(game.team1.all())
        team2 = set(game.team2.all())


        if (player in team1):
            if game.victors == 0: # check for wins BUG
                for opp_player in team2:
                    if opp_player not in wins_dict:
                        wins_dict[opp_player] = 1
                    else:
                        wins_dict[opp_player] += 1

            else:
                for opp_player in team2:
                    if opp_player not in loss_dict:
                        loss_dict[opp_player] = 1
                    else:
                        loss_dict[opp_player] += 1

        if (player in team2):
            if game.victors == 1: # check for wins BUG
                for opp_player in team1:
                    if opp_player not in wins_dict:
                        wins_dict[opp_player] = 1
                    else:
                        wins_dict[opp_player] += 1

            else:
                for opp_player in team1:
                    if opp_player not in loss_dict:
                        loss_dict[opp_player] = 1
                    else:
                        loss_dict[opp_player] += 1

    nemesis = max(loss_dict, key=loss_dict.get)
    bitch = max(wins_dict, key=wins_dict.get)


    context = {'player': player, 'datax': datax, 'datay': datay, 'nemesis':nemesis, 'bitch':bitch}
    return HttpResponse(template.render(context, request))
