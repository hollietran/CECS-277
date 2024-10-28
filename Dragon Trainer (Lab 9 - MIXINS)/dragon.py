from entity import Entity
import random

class Dragon(Entity):
    def __init__(self, name, max_hp, num_sp):
        # call super's init, then set _special_attacks
        super().__init__(name, max_hp)
        self._special_attack = num_sp
    
    def decrement_special(self):
        # subtract 1 from _special_attack
        self._special_attack -= 1
    
        # If the value <0, reset it to 0
        if self._special_attack < 0:
            self._special_attack =  0  

    def basic_attack(self, opponent):
        # Tail attack: the hero takes a random amount of dmg (3~7)
        dmg = random.randint(3,7)
        self._hp -= dmg

        # Return a string with the description of the attack and dmg dealt to hero
        return f'{self.name} strikes with its tail, dealing {dmg} damage to {opponent.name}!'
    
    @property
    def special_attacks(self):
        return self._special_attack

    def __str__(self):
        # use the super to get the __str__ from entity
        # concatanate on the number of special attacks remaining
        return f'{super().__str__()} | Special Attacks Left: {self._special_attack}'
