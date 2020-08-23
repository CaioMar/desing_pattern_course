from abc import ABC, abstractmethod

class Creature:
    def __init__(self, attack, health):
        self.health = health
        self.attack = attack

class CardGame(ABC):
    def __init__(self, creatures):
        self.creatures = creatures

    # return -1 if both creatures alive or both dead after combat
    # otherwise, return the _index_ of winning creature
    def combat(self, c1_index, c2_index):
        
        print(self.creatures[c1_index].health, self.creatures[c2_index].health)

        c2_health = self.hit(self.creatures[c1_index], self.creatures[c2_index])
        
        c1_health = self.hit(self.creatures[c2_index], self.creatures[c1_index])

        print(c1_health, c2_health)

        if (c1_health > 0 and c2_health > 0) or ((c1_health <= 0 and c2_health <= 0)):
            return -1
        
        if c1_health > 0:
            return c1_index
        return c2_index

    @abstractmethod
    def hit(self, attacker, defender):
        pass  # implement this in derived classes


class TemporaryDamageCardGame(CardGame):

    def hit(self, attacker, defender):
        return defender.health - attacker.attack


class PermanentDamageCardGame(CardGame):

    def hit(self, attacker, defender):
        def_health = defender.health - attacker.attack
        defender.health = def_health
        return def_health


if __name__ == "__main__":
    list_of_creatures = [Creature(1,5),Creature(2,2)]
    magic = TemporaryDamageCardGame(list_of_creatures)
    print("1st round Magic combat: %d" %magic.combat(0,1))
    print("2nd round Magic combat: %d" %magic.combat(0,1))


    hearthstone = PermanentDamageCardGame(list_of_creatures)
    print("1st round Hearthstone combat: %d" %hearthstone.combat(0,1))
    print("2nd round Hearthstone combat: %d" %hearthstone.combat(0,1))