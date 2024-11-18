from abc import ABC, abstractmethod

class DoorFactory(ABC):
    
    @abstractmethod
    def create_door(self):
        # Creates and return a door instance.
        pass