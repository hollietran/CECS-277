import random
from door import Door

class CodeDoor(Door):
    """
    Locked door: randomize the location of the key. 3 possibility
    """
    
    def __init__(self):
        self._solution = [bool(random.choice(["X", "O"]) == "X") for _ in range(3)]
        self._attempts = [bool(random.choice(["X", "O"]) == "X") for _ in range(3)]
    
    @property
    def solution(self):
        return self._solution
    
    @property
    def attempts(self):
        return self._attempts
    
    def examine_door(self):
        return "A door with a coded keypad with three characters. Each Key toggles a value with an 'X' or an 'O'."
    
    def menu_options(self):
        return '1. Press Key 1.\n2. Press Key 2.\n3. Press Key 3.\n'
    
    def get_menu_max(self):
        return 3

    def attempt(self, option):
        attempts_display = ['X' if attempt else 'O' for attempt in self.attempts]
        print(f'[{attempts_display[0]} {attempts_display[1]} {attempts_display[2]}]')

        if option == 1:
            self.attempts[0] = not self.attempts[0]
        elif option == 2:
            self.attempts[1] = not self.attempts[1]
        else:
            self.attempts[2] = not self.attempts[2]
        return ""
    def is_unlocked(self):
        if self.attempts == self.solution:
            return 'You found the correct code!'

    def clue(self):
        count = 0
        for i in range(3):
           if self.solution[i] == self.attempts[i]:
               count += 1

        return f"You currently have {count} number of keys correct."
    
    def success(self):
        return "Congratulations, you opened the door!"