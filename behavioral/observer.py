class Event(list):
    def __call__(self, *args, **kwargs):
        for item in self:
            item(*args, **kwargs)


class Game:
    def __init__(self):
        self.attack_change = Event()


class Rat:
    def __init__(self, game):
        self.game = game
        self._attack = 1
        self.game.attack_change.append(self.rat_bonus)

    @property
    def attack(self):
        self.game.attack_change(self)
        return self._attack

    def rat_bonus(self, value):
        if self == value:
            self._attack = len(self.game.attack_change)

    def __enter__(self):
        return self

    def __exit__(self, exception_type, exception_value, traceback):
        self.game.attack_change.remove(self.rat_bonus)

    def __str__(self):
        return "Rat attack value {}.".format(self.attack)


if __name__ == "__main__":
    game = Game()

    rat = Rat(game)

    print(rat)

    rat2 = Rat(game)

    print(rat)
    print(rat2)

    with Rat(game) as rat3:
        print(rat)
        print(rat2)
        print(rat3)

    print(rat)
    print(rat2)