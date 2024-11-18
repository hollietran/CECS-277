import random
from door import Door

class LockedDoor(Door):
    """
    Locked door: randomize the location of the key. 3 possibility
    """
    
    def __init__(self):
        self._solution = random.randint(1,3)
        self._unlocked = False

    @property
    def solution(self):
        return self._solution
    
    @property
    def unlocked(self):
        return self._unlocked
    
    def examine_door(self):
        return "A locked door. Look around, the key is hidden nearby."
    
    def menu_options(self):
        return '1. Look under the mat\n2. Look under the flower pot.\n3. Look under the fake rock.\nEnter Choice: '
    
    def get_menu_max(self):
        return 3

    def attempt(self, option):
        messages = {
            1: "You look under the mat.",
            2: "You look under the flower pot.",
            3: "You look under the fake rock.",
        }

        # Retrieve the message based on the option
        message = messages.get(option, "Invalid option")
        print(message)
        
        if option == self.solution:
            self._unlocked = True
            return "You found the key!"
        else: 
            return "You didn't find the key, try somewhere else."
    
    def is_unlocked(self):
        return self.unlocked

    def clue(self):
        return "Try the another place"
    
    def success(self):
        return "Congratulations, you opened the door!"