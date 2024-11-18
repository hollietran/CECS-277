import random
from door import Door

class BasicDoor(Door):
    """
    Basic door: randomize the solution to either push or pull
    """
    
    def __init__(self):
        self._solution = random.choice(["push", "pull"])
        self._attempts = None
    
    def examine_door(self):
        return "A basic door. You can either push or pull it to open."
    
    def menu_options(self):
        return '1. Push\n2. Pull\n Enter Choice: '
    
    def get_menu_max(self):
        return 2
    
    def attempt(self, option):
        self.attempts = option
        self.attempts = "push" if option == 1 else "pull"
        return f"You attempt to {self.attempts} the door."
    
    def is_unlocked(self):
        return self.attempts == self._solution

    def clue(self):
        return "Try the other way"
    
    def success(self):
        return "Congratulations, you opened the door!"