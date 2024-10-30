from entity import Entity
import random

class Enemy(Entity):
    def __init__(self):
        # Randomize a name from a list of names (Ex: Goblin, Vampire, Ghoul, Skeleton, Zombie, etc)
        names = ["Goblin", "Vampire", "Ghoul", "Skeleton", "Zombie"]
        name = random.choice(names)
        max_hp = random.randint(4,8)
        super().__init__(name, max_hp)

    def attack(self, entity):
        # Random damage in range of 1~4
        damage = random.randint(1,4)
        entity.take_damage(damage)
        # Return a string that shows the event that occured
        return f'{self.name} attacks {entity.name} for {damage} damage.'
