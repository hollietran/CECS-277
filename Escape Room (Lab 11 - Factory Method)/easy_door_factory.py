import random
from door_factory import DoorFactory
from basic_door import BasicDoor
from locked_door import LockedDoor
from combo_door import ComboDoor

class EasyDoorFactory(DoorFactory):
    def create_door(self):
        # Creates and return a door instance.
        return random.choice([BasicDoor(), LockedDoor(), ComboDoor()])
