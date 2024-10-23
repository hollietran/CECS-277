import die

class Player:
    def __init__(self):
        # Constructs and sort the list of three Die objects and initializes the player's points to 0
        self.dice_list = [self.d1, self.d2, self.d3]
        self.point = 0

    def get_points(self):
        # Returns the player's points.
        return self.point
    
    def roll_dice(self):
        # Calls roll on each of the Die objects in the dice list and sorts the list
        self.d1 = die.roll()
        self.d2 = die.roll()
        self.d3 = die.roll()
        sorted_dice_list = sorted(self.dice_list)

    def has_pair(self):
        # returns true if two dice in the list have the same value, Increments points by 3
        if (self.d1 == self.d2) or (self.d1 == self.d3) or (self.d2 == self.d3):
            self.point += 3
            return True
        else:
            return False
    
    def has_three_of_a_kind(self):
        # Returns true if all three dice in the list have the same values. Increments points by 3
        if self.d1 == self.d2 == self.d3:
            self.point += 3
            return True
        else:
            return False
    
    def has_series(self):
        # Returns true if the values of each of the dice in the list are in a sequence. Incerments points by 2
        return all(sorted_dice[i] + 1 == sorted_dice[i+1] for i in range(len(sorted_dice)-1))
    def __str__(self):
        # Returns a string in the format "D1 = _, D2 = _, D3= _"
        return f'D1 = {self.d1}, D2 = {self.d2}, D3 = {self.d3}'