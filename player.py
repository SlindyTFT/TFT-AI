from unit import Unit

class Player:
    def __init__(self):
        self.shop: list[Unit] = [None] * 5
        self.gold = 0
        self.items: list[str] = []
        self.bench: list[Unit] = [None] * 9
        self.board: list[Unit] = [None] * 10

    
    def purchase_champ(self, position: int):
        unit = self.shop[position]
        if (self._add_to_bench(unit) is None):
            self.gold = self.gold - unit.cost
        
    def _load_shop(self, units: list[Unit]):
        self.shop = units
        print(units[0])
        print(units)


    def _add_to_bench(self, champion: Unit):
        for i, champ in enumerate(self.bench):
            if champ is None:
                self.bench[i] = champion
                return None
        return champion
    
    def show_bench(self):
        return self.bench

    def show_shop(self):
        return self.shop

    

        


