#Broker Chain

from abc import ABC
from enum import Enum

class Event(list):
    def __call__(self, *args, **kwargs):
        for item in self:
            item(*args, **kwargs)


class WhatToQuery(Enum):
    ATTACK = 1
    DEFENSE = 2


class Query:
    def __init__(self, creature_name, what_to_query, default_value):
        self.value = default_value
        self.what_to_query = what_to_query
        self.creature_name = creature_name


class Creature:

    def __init__(self, game, name, attack, defense):
        self.initial_defense = defense
        self.initial_attack = attack
        self.name = name
        self.game = game

    @property
    def attack(self):
        q = Query(self.name, WhatToQuery.ATTACK, self.initial_attack)
        self.game.perform_query(self, q)
        return q.value

    @property
    def defense(self):
        q = Query(self.name, WhatToQuery.DEFENSE, self.initial_defense)
        self.game.perform_query(self, q)
        return q.value

    def __str__(self):
        return '{} ({}/{})'.format(self.name, self.attack, self.defense)

class CreatureModifier(ABC):
    def __init__(self, game, creature):
        self.creature = creature
        self.game = game
        self.game.queries.append(self.handle)

    def handle(self, sender, query):
        pass

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.game.queries.remove(self.handle)


class Goblin(Creature, CreatureModifier):
    def __init__(self, game, name='Goblin', attack=1, defense=1):
        super().__init__(game=game,
                         name=name,
                         attack=attack,
                         defense=defense)        
        self.game.creatures.append(self)
        self.game.queries.append(self.handle)

    def handle(self, sender, query):
        if sender == self:
            if query.what_to_query == WhatToQuery.DEFENSE:
                number_of_goblins = len(['Goblin' 
                                        for creature in self.game.creatures
                                        if creature.name.startswith('Goblin')])
                query.value += number_of_goblins
            if query.what_to_query == WhatToQuery.ATTACK:
                number_of_goblins_kings = len(['GoblinKing' 
                                                for creature in self.game.creatures
                                                if creature.name.startswith('GoblinKing')])
                print(number_of_goblins_kings)
                query.value += number_of_goblins_kings


class GoblinKing(Goblin, CreatureModifier):
    def __init__(self, game):
        super().__init__(game=game,
                         name='GoblinKing',
                         attack=3,
                         defense=3)        

    def handle(self, sender, query):
        super().handle(sender, query)

class Game:
    def __init__(self):
        self.creatures = []
        self.queries = Event()

    def perform_query(self, sender, query):
        self.queries(sender, query)

if __name__ == "__main__":
    game = Game()
    goblin = Goblin(game)
    print(goblin)

    goblin2 = Goblin(game)

    print(goblin2)

    goblink = GoblinKing(game)

    print(goblin2, goblink)



