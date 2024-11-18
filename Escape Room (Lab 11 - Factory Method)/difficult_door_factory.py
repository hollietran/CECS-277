import random
from door_factory import DoorFactory
from combo_door import ComboDoor
from deadbolt_door import DeadboltDoor
from code_door import CodeDoor

class DifficultDoorFactory(DoorFactory):
    def create_door(self):
        # Creates and return a door instance.
        return random.choice([ComboDoor(), DeadboltDoor(), CodeDoor()])
