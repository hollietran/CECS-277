import random
import check_input
from entity import Entity

class Hero(Entity):
    def basic_attack(self, opponent):
        # The dragon takes a random amount of dmg (2 D6: 1~6 + 1~6)
        # Returns a string with the description of the attack and the dmage dealt to the dragon
        damage = random.randint(1,6) + random.randint(1,6)
        opponent.take_damage(damage)
        return f"{self.name} slashes {opponent.name} with their sword for {damage} damage!"


    def special_attack(self, opponent):
        # The dragon takes a random amount of dmg (1 D12: 1~12)
        # Return the string with the description of the attack and dmg dealt to the dragon
        damage = random.randint(1,12)
        opponent.take_damage(damage)
        return f"{self.name} stricked {opponent.name} with a powerful blow for {damage} damage"
