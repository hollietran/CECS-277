from dragon import Dragon
from flying import Flying
import random

class FlyingDragon(Dragon, Flying):
    def __init__(self):
        #call super to set a default name, hp, and number of special attacks
        super().__init__("Timberjack", 10, 3)
        # self._special_attack = 3

    def special_attack(self, oppoonent):
        #Randomly choose one of the two flying attacks methods from Flying mixin
        choice = random.randint(1,2)
        if choice == 1:
            self.swoop(oppoonent)
        else:
            self.windblast(oppoonent)

        