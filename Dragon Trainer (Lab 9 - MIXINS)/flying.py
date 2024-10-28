import random

class Flying():
    def swoop(self, opponent):
        # if the dragon has any special attacks left
        if self.special_attacks > 0:
            # then it does a swoop attack at the hero and they take a random amount of damage in the range 4-8
            swoop_damage = random.randint(4,8)
            opponent.take_damage(swoop_damage)
            # the number of special attacks is decremented. 
            self.decrement_special()
            # Return a string with a description of the attack and the damage dealt to the hero. 
            return f"{self.name} swoops down on {opponent.name}, dealing {swoop_damage} damage!"
        else:
            # Otherwise, no damage is done and a string describing the failure is returned.
            return f"{self.name} tries to swoop, but it is too tired to perform any special attacks."

    def windblast(self, opponent):
        # if the dragon has any special attacks left, then it blasts wind at the hero
        if self.special_attacks > 0:
            # they take a random amount of damage in the range 3-7 
            windblast_damage = random.randint(3,7)
            opponent.take_damage(windblast_damage)
            # the number of special attacks is decremented
            self.decrement_special()
            # Return a string with a description of the attack and the damage dealt to the hero. 
            return f"{self.name} blasts {opponent.name} with wind, dealing {windblast_damage} damage!"
        else:
            # Otherwise, no damage is done and a string describing the failure is returned
            return f"{self.name} tries to blast wind, but it is too tired to perform special attacks."