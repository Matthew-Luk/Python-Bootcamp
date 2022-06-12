from classes.ninja import Ninja
from classes.pirate import Pirate
import random

michelangelo = Ninja("Michelanglo")
jack_sparrow = Pirate("Jack Sparrow")

class Game:
    def __init__(self, pirate, ninja):
        self.pirate = pirate
        self.ninja = ninja

    def play(self):
        while self.pirate.health > 0 and self.ninja.health > 0:
            turn = (random.randint(1,8))
            if turn <= 5:
                michelangelo.attack(jack_sparrow)
                print(f"Ninja attacked Pirate - Pirate Health: {self.pirate.health}")
            elif turn > 5:
                jack_sparrow.attack(michelangelo)
                print(f"Pirate attacked Ninja - Ninja Health: {self.ninja.health}")

    def winner(self):
        if self.pirate.health <= 0:
            print("Ninja won")
            return self
        elif self.ninja.health <= 0:
            print("Pirate won")
            return self

x = Game(jack_sparrow,michelangelo)
jack_sparrow.show_stats()
michelangelo.show_stats()
x.play()
x.winner()