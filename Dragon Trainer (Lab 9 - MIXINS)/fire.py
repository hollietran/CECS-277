import random

class Fire:
    def fireblast(self, opponent):
        # if the dragon has any special attacks left, then blast hero with fire: take dmg (5~9)
        if self.special_attacks > 0:
            fireblast_dmg = random.randint(5,9)
            opponent.take_damage(fireblast_dmg)

            # number of special attack is decremented
            self.decrement_special()
            # Return a string with a description of attack dealt to hero
            return f'{self.name} engulfs {opponent.name} in flames for {fireblast_dmg} damage!'
        # Otherwise no dmg done --> return string describing failure
        else:
            return f"{self.name} tries to engulf {opponent.name} in flames, but it's all out of fuel"
        

    def fireball(self, opponent):
        # If dragon has special attacks left, then it spits a fireball at the hero: take dmg (4~8)
        if self.special_attacks > 0:
            fireball_dmg = random.randint(4, 8)
            opponent.take_damage(fireball_dmg)

            # number of special attack is decremented
            self.decrement_special()
    
        # Return string with description of attack
            return f"{self.name} spits a fireball at {opponent.name} for {fireball_dmg} damage!"
        
        # Otherwise no dmg done --> return string describing failure
        else:
            return f"{self.name} tries to spit a fireball at {opponent.name} but it's all out of fuel"
    
    