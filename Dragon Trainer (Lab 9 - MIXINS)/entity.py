from abc import ABC, abstractmethod
import random


class Entity(ABC):
    def __init__(self, name, max_hp):
        # Set the _name, _max_hp, and _hp
        # Assign the max_hp value to both the _max_hp and _hp attributes
        self._name = name
        self._max_hp = max_hp
        self._hp = max_hp

    # name and hp properties uses decorators to get the values of _name and _hp.
    @property
    def name(self):
        return self._name
    
    @property
    def hp(self):
        return self._hp
    
    
    def take_damage(self, dmg):
        # Subtract the dmg value from the entity's _hp
        self._hp -= dmg

        # If hp falls less then 0, reset it to be 0
        if self._hp < 0:
            self._hp = 0

    def __str__(self):
        # Returns the entity's name and hp in the fromat:
        #"Name: hp/max_hp".
        return f'{self._name}: {self._hp}/{self._max_hp}'

    @abstractmethod
    def basic_attack(self, opponent):
        pass

    @abstractmethod
    def special_attack(self, opponent):
        pass

