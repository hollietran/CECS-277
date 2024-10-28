from dragon import Dragon
from fire import Fire 
import random

class FireDragon(Dragon, Fire):
    def __init__(self):
        #call super to set a default name, hp and numbers of special attacks
        super().__init__("Gronkle", 15, 2)
        
        

    def special_attack(self, opponent):
        # Randomly choose one of the two fire attack methods from Fire mixin
        choice = random.randint(1,2)
        if choice == 1:
            self.fireball(opponent)
        else:
            self.fireblast(opponent)

