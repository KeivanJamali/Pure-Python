import math


class Lig:
    def __init__(self):
        self.teams = {}
        self.players = []

    def new_team(self, team_name: str) -> None:
        if team_name in self.teams:
            print("team with this name already exists")
        else:
            self.teams[team_name] = {"power": 0, "score": 0, "goal_difference": 0, "players": {}}
            print("new team created successfully!")

    def new_player(self, player_name: str, power: int, team_name: str) -> None:
        if player_name not in self.players:
            if team_name in self.teams:
                self.teams[team_name]["players"][player_name] = power
                self.teams[team_name]["power"] += power
                self.players.append(player_name)
                print("new player created successfully!")
            else:
                print("team with this name does not exist")
        else:
            print("player with this name already exists")

    def new_game(self, team_name1: str, team_name2: str) -> None:
        if team_name1 in self.teams and team_name2 in self.teams:
            critical_num = int(self.teams[team_name1]["power"] - (self.teams[team_name2]["power"]) * 0.2)
            if critical_num > 0:
                self.teams[team_name1]["score"] += 10
                self.teams[team_name1]["goal_difference"] += abs(critical_num)
                self.teams[team_name2]["goal_difference"] -= abs(critical_num)
                print(f"the {team_name1} won the game")
            elif critical_num < 0:
                self.teams[team_name2]["score"] += 10
                self.teams[team_name2]["goal_difference"] += abs(critical_num)
                self.teams[team_name1]["goal_difference"] -= abs(critical_num)
                print(f"the {team_name2} won the game")
            elif critical_num == 0:
                self.teams[team_name1]["score"] += 5
                self.teams[team_name2]["score"] += 5
                print("the teams were tied")
        else:
            print("there is no team with these names")

    def league_table(self) -> None:
        sorted_teams = sorted(self.teams,
                              key=lambda x: (-self.teams[x]["score"], -self.teams[x]["goal_difference"], x))

        for team in sorted_teams:
            print(f"{team} {self.teams[team]['score']} {self.teams[team]['goal_difference']}")

    def team_players(self, team_name: str) -> None:
        if team_name in self.teams:
            sorted_players = sorted(self.teams[team_name]["players"],
                                    key=lambda x: (self.teams[team_name]["players"][x], x))
            for player in sorted_players:
                print(f"{player} {self.teams[team_name]['players'][player]}")
        else:
            print("team with this name does not exist")


main = Lig()

while True:
    read = input()
    command = read.split()
    if command[0] == "new_team":
        main.new_team(command[1])
    elif command[0] == "new_player":
        main.new_player(command[1], int(command[2]), command[3])
    elif command[0] == "new_game":
        main.new_game(command[1], command[2])
    elif command[0] == "league_table":
        main.league_table()
    elif command[0] == "team_players":
        main.team_players(command[1])
    elif command[0] == "end":
        break
    else:
        print("invalid command")
