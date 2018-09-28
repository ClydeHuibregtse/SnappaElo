
from  django import forms
from .models import *





class GameForm(forms.Form):
    # pass

    choices = [(0,"--------")] + [(x,x) for x in Player.objects.all()]

    player0 = forms.ChoiceField(choices=choices, label='Player1 (Team1)')
    player1 = forms.ChoiceField(choices=choices, label='Player2 (Team1)')
    player2 = forms.ChoiceField(choices=choices, label='Player3 (Team2)')
    player3 = forms.ChoiceField(choices=choices, label='Player4 (Team2)')


    score0 = forms.IntegerField(label='Team1 Score')
    score1 = forms.IntegerField(label='Team2 Score')

    note = forms.CharField(label='Notes', max_length=250)
