class Team:
    def __init__(self, name, city, rank):
        self.name = name
        self.city = city
        self.rank = rank

    def __str__(self):
        return "{} {}".format(self.city, self.name)


class Game:
    def __init__(self, team_1, team_2):
        self.home_team = team_1
        self.visiting_team = team_2

    def __str__(self):
        return "Welcome to a game between the {}d {} and the {}d {}".format(self.home_team.rank, self.home_team, self.visiting_team.rank, self.visiting_team)

team_1 = Team("Astros", "Houston", "3rd place")
print(team_1)
team_2 = Team("Yankees", "New York", "5th place")
print(team_2)

game = Game(team_1, team_2)

print(game)