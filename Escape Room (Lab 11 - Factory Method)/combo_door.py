import random
from door import Door

class ComboDoor(Door):
    """
    Locked door: randomize the location of the key. 3 possibility
    """
    
    def __init__(self):
        self._solution = random.randint(1,10)
        self._attempts = None

    @property
    def solution(self):
        return self._solution
    
    @property
    def attempts(self):
        return self._attempts
    
    def examine_door(self):
        return "A door with a combination lock. You can spin the dial to a number 1-10."
    
    def menu_options(self):
        return "Enter # 1-10: "
    
    def get_menu_max(self):
        return 10

    def attempt(self, option):
        self._attempts = option
        return f'You turn the dial to {self.attempts}'
    
    def is_unlocked(self):
        if self.attempts == self.solution:
            return 'You found the correct number'

    def clue(self):
        if self.attempts > self.solution:
            return "Too high."
        else:
            return "Too low"
    
    def success(self):
        return "Congratulations, you opened the door!"