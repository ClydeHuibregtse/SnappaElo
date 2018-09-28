
from elo.models import *

brothers = ["Brandon McKenzie",
            "Jini Gabbidon",
            "Peter Calvaresi",
            "Joshua Graves",
            "Andy Rodriguez",
            "Tim Kralj",
            "Justin Xiang",
            "Justin Chiu",
            "Federico Bescotti",
            "Clyde Huibregtse",
            "Kaiko Manson",
            "Matt Woicik",
            "Gabe Schneider",
            "Nikhil Bhatia",
            "Luka Knezevic",
            "Sam Bockman",
            "AJ Jurko",
            "Chris Xue",
            "Brad Jomard",
            "Emilio Sison",
            "Jeremy Noel",
            "Ben Teitscheid",
            "Johnny Reece",
            "Daniel Shkreli",
            "Grant Fuhr",
            "Miguel Lamar",
            "Kevin Downey",
            "Evan Kim",
            "Ian Hinkley",
            "Christian Hwa",
            "Miller Geschke",
            "Kwet Okine",
            "Patroklos Stefanou",
            "Kyle Sandell",
            "John Steele",
            "Kaden DiMarco",
            "Giannis Chatziveroglou",
            "Brett Allen",
            "Alex Cho",
            "Jordan Ren",
            "Cooper Driscoll"
            ]

for bro in brothers:
    player_to_add = Player(name=bro)
    player_to_add.save()
