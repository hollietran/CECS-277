from abc import ABC, abstractmethod

class Door(ABC):
    @abstractmethod
    def examine_door(self):
        # returns a string description of the door
        pass

    @abstractmethod
    def menu_options(self):
        # returns a string with the menu option that the user can choose from when attempting to unlock the door.
        pass

    @abstractmethod
    def get_menu_max(self):
        # returns the number of options in the above menu for check input
        pass

    @abstractmethod
    def attempt(self, option):
        # passes user's menu selection
        # Use this value to update the input attribute
        # return a string describing the user's attempt
        pass

    @abstractmethod
    def is_unlocked(self):
        # checks if the door was unlocked by comparing the input attribute with the solution
        # returns True if it is unlocked, False otherwise.
        pass

    @abstractmethod
    def clue(self):
        # returns a hint for the user if their attempt was unsuccessful
        pass

    @abstractmethod
    def success(self):
        # returns a congratulatory message if the user attempt was successful
        pass

