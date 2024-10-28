import dragon, fire, flying, random

class FlyingFireDragon(dragon.Dragon, fire.Fire, flying.Flying):
    def __init__(self):
        super().__init__("Deadly Nadder", 30, 2)

    def special_attack(self, oppoonent):
        #Randomly choose one of the two flying attacks methods from Flying mixin
        choice = random.randint(1,4)
        if choice == 1:
            self.swoop(oppoonent)
        elif choice == 2:
            self.windblast(oppoonent)
        elif choice == 3:
            self.fireball(oppoonent)
        else:
            self.fireblast(oppoonent)