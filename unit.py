class Unit:
    def __init__(self, name: str, cost: int, traits: list[str]):
        self.name = name
        self.cost = cost
        self.traits = traits


    def __str__(self):
        return self.name
    
    def __repr__ (self):
        return self.name



