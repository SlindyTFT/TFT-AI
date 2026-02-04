class Unit:
    def __init__(self, name: str, cost: int, traits: list[str]):
        self.name = name
        self.level = 1
        self.cost = cost
        self.traits = traits

    def get_name(self):
        return self.name

    def get_cost(self):
        return self.cost

    def get_traits(self):
        return self.traits

    def get_level(self):
        return self.level

    def set_level(self, level: int):
        self.level = level

    def leveled_up(self):
        new_unit = Unit(self.name, self.cost, self.traits)
        new_unit.set_level(self.level + 1)
        return new_unit

    def get_total_units(self):
        return 3**(self.level - 1)

    def __str__(self):
        return f'{self.level}* {self.name}'
    
    def __repr__ (self):
        return f'{self.level}* {self.name}'

    def __eq__(self, other):
        if other is not None:
            if type(other) is type(self):
                return self.name == other.name and self.level == other.level
        return False

    def __copy__(self):
        new_unit = Unit(self.name, self.cost, self.traits)
        new_unit.set_level(self.level)
        return new_unit


