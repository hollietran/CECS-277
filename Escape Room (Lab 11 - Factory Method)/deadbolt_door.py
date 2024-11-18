from door import Door
import random

class DeadboltDoor(Door):
    def __init__(self):
        super().__init__()
        self._solution = [random.choice([True, False]), random.choice([True, False])]
        self._attempts = None
    
    @property
    def solution(self):
        return self._solution
    
    @property
    def attempts(self):
        return self._attempts
    
    def examine_door(self):
        return "A double deadbolt door. Both need to be unlocked to open the door, but you can't tell by looking at them if they are locked or unlocked."
    
    def menu_options(self):
        return '1. Toggle bolt 1\n2. Toggle bolt 2\n'
    
    def get_menu_max(self):
        return 2
    
    def attempt(self, option):
        if option in (1,2):
            bolt_index = option - 1
            self._solution[bolt_index] = not self._solution[bolt_index]
            return f"You toggled bolt {option}."
        else:
            return "Invalid option. Please choose 1 or 2."
    
    def is_unlocked(self):
        return all(self.solution)

    def clue(self):
        """Provide a clue based on the state of the bolts."""
        if all(bolt == False for bolt in self._solution):
            # If both bolts are still locked
            return "You jiggle the door... it seems like it's completely locked."
        elif any(bolt == True for bolt in self._solution):
            # If one of the bolts is unlocked
            return "You jiggle the door... it seems like one of the bolts is unlocked."
        else:
            # This should not be hit, but as a fallback
            return "The bolts seem to be in an unknown state."
        
    
    def success(self):
        return "Congratulations, you opened the door!"