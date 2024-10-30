from abc import ABC, abstractmethod

class Entity:
    def __init__(self, name, max_hp):
        # Initilize each of the instances variables
        self._name = name
        self._max_hp = max_hp
        self._hp = max_hp

    @property
    def name(self):
        return self._name
    
    @property
    def hp(self):
        return self._hp

    def take_damage(self, dmg):
        # subtracts the dmg from the hp, but does not allow the hp to drop below 0
        self._hp -= dmg
        if self._hp < 0:
            self._hp = 0
    
    def heal(self): 
        # restors the entity's hp to max_hp
        self._hp = self._max_hp

    def __str__(self):
        # Returns a string in the format 'Name\nHP: hp/max_hp'
        return f'Name: {self._name}\nHP: {self._hp}/{self._max_hp}'

    @abstractmethod
    def attack(self, entity):
        pass