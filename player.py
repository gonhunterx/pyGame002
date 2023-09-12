class Player:
    def __init__(self, name):
        self.name = name
        self.health = 10
        self.damage = 2
        self.totalExp = 0
        self.woodCuttingexp = 0

    def displayStats(self):
        print(f"player name: {self.name}")
        print(f"health: {self.health}")
        print(f"experience: {self.totalExp}")
