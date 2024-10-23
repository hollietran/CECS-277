import random

class Die:
    """
    Attributes:
        sides (int): number of sides on the die.
        value (int): the value of the rolled die.
    """

    def __init__(self, sides=6):
        #Sets the number of sides to the die (default 6)
        self.sides = sides
        self.value = self.roll()

    def roll(self):
        # Retruns the rolled value of die
        self.value = random.randint(1, self.sides)
        return self.value

    def __str__(self):
        # Returns the string of the die value.
        return str(self.value)

    def __lt__(self, other):
        # Returns wheter value of self is less then the value of other
        return self.value < other.value

    def __eq__(self, other):
        # Returns whether value of self is equal to that of other
        return self.value == other.value
    
    def __sub__(self, other):
        # Returns the difference in value between self and other.
        return self.value - self.other