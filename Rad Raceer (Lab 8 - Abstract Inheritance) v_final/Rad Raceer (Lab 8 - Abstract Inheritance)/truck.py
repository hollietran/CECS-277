import vehicle
import random

class Truck(vehicle.Vehicle):
    def __init__(self):
        # calls the superclass's init with values for name ("Behemoth Truck"), intial ("T"), min_speed (4), max_speed (8).
        super().__init__("Behemoth Truck", "T", 4, 8)
        
    
    def description_string(self):
        # returns a string with the truck's stats and abilities
        return f"{self.name} - a heavy truck ({self.min_speed}-{self.max_speed}) units. Special: Ram (2x speed and it smashes through obstacles)."
    
    def special_move(self, dist):
        # dist == distance to next obstacle
        # if energy >= 15, energy-15, move truck 2x speed, if obstacle in the way ("ram", bashes through the obstacle)
        if self.energy < 15:
            return f"{self.name} does not have eneough energy to use Ram!"
        else:
            self.energy -= 15
            movement = random.randint(self.min_speed, self.max_speed) * 2
            self.position += movement

            if self.position == dist:
                return f"{self.name} rams forward bashing through the Obstacle to go {movement} units!"
        # return a string that describes the event that occured.
        return f"{self.name} rams forward {movement} units!"
    