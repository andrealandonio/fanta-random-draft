class Player:
    def __init__(self, name, team, price):
        self.name = name
        self.team = team
        self.price = price
    
    def show(self):
        print(self.name + " (" + self.team + ", " + str(self.price) + ")")