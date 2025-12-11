from unit import Unit
from typing import Optional, List

class Player:
    def __init__(self):
        self.shop: list[Optional[Unit]] = [None] * 5
        self.gold = 3
        self.items: list[str] = []
        self.bench: list[Optional[Unit]] = [None] * 9
        self.board: list[Optional[Unit]] = [None] * 10

    
    def purchase_champ(self, position: int):
        unit = self.shop[position]
        if self.gold > unit.cost:
            if self._add_to_bench(unit) is None:
                self.gold = self.gold - unit.cost
                return unit
        return None
        
    def _load_shop(self, units: list[Optional[Unit]]):
        self.shop = units
        # print(units[0])
        # print(units)


    def _add_to_bench(self, champion: Unit):
        for i, champ in enumerate(self.bench):
            if champ is None:
                self.bench[i] = champion
                self.shop[i] = None
                return None
        return champion
    
    def show_bench(self):
        return self.bench

    def show_shop(self):
        return self.shop

    def roll_shop(self):
        if self.gold >= 2:
            self.gold = self.gold - 2
            self.shop = [None] * 5
            return None
        return self.shop

    def show_gold(self):
        return self.gold

    

        


