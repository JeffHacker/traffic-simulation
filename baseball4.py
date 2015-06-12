import random

class Team:
    def __init__(self, name, city, rank, stadium):
        self.name = name
        self.city = city
        self.rank = rank
        self.stadium = stadium

    def __str__(self):
        return "{} {}".format(self.city, self.name)

class Game:
    def __init__(self, team_1, team_2):
        self.home_team = team_1
        self.visiting_team = team_2

    def __str__(self):
        return "WELCOME to {}, the home of the {}d {}.  Tonight they will be playing against the {}d {}.".format\
            (self.home_team.stadium, self.home_team.rank, self.home_team, self.visiting_team.rank, self.visiting_team)

'''class TeamData: #this isn't how I should do this I think.  I should do sub-classes
    def __init__(self):
        self.random_team_1 = random.rand

        team_info = [["Cubs", "Chicago", "last place", "Wrigley Field"],
                     ["Royals", "Kansas City", "first place", "The 'K', Kaufman Stadium"],
                     ["Cardinals", "St. Louis", "fifth place", "Busch Stadium"],
                     ["Astros", "Houston", "forth place", "Minute Maid Park"],
                     ["Padres", "San Diego", "second place", "Petco Park"],
                     ["Yankees", "New York", "third place", "Yankee Stadium"]
                       ]'''

# ok I see an alert here mentioning that I'm missing a Super... but it still works so I'm curious
class Cubs(Team):  #not sure about this
    def __init__(self):
        self.name = "Cubs"
        self.city = "Chicago"
        self.rank = "last place"
        self.stadium = "Wrigley Field"




# standard team entry
team_1 = Team("Astros", "Houston", "3rd place", "Minute Maid Park")
print(team_1)

# attempting toward auto entry for use with random choice for team
# t1 = ["Cubs", "Chicago", "last place", "Wrigley Field"]
# team_2 = Team(t1)

# attempting a subclass to create a team... SUCCESS!
team_2 = Cubs()
print(team_2)

game = Game(team_1, team_2)
print(game)