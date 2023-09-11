from player import Player

class Manager:
    TEAM_PLAYERS = 25

    def __init__(self, name, budget) -> None:
        self.name = name
        self.budget = budget
        self.players = []

    def show(self) -> None:
        print(self.name + " (" + str(self.get_remaining_budget()) + ")")
        for player in self.players:
            player.show()

    def add_player(self, player) -> None:
        self.players.append(player)
    
    def get_remaining_budget(self) -> int:
        remaining_budget = self.budget
        for player in self.players:
            remaining_budget = remaining_budget - player.price
        return remaining_budget
    
    def get_remaining_players(self) -> int:
        return self.TEAM_PLAYERS - len(self.players)