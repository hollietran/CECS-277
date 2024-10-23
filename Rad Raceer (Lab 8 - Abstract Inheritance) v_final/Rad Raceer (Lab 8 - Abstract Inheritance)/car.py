import check_input
import random
from vehicle import Vehicle
from abc import abstractmethod

class Car(Vehicle):
    def __init__(self):
        # calls the superclass’s init with values for name (“Lightning Car”),
        # initial (‘C’), min_speed (6), and max_speed (8)
        super().__init__('Lightning Car', 'C', 6, 8)
        

    def description_string(self):
        return f'{self.name} a fast car ({self.min_speed}-{self.max_speed} units). Special: Nitro Boost (1.5x speed)'

    def special_move(self, dist):
        """passes in the distance to the next obstacle (if there is one). 
        If there is sufficient energy (>= 15), deduct 15 energy and move the car at 1.5x speed. 
        If there is an obstacle, then it will crash and stops in the space just before it,
        otherwise it moves the randomized distance. Return a string that describes the event that
        occurred with the name of the car and the distance traveled (if applicable)."""
        if self.energy >= 15: 
            self.energy -= 15

            # 1.5x boost
            base_speed = random.randint(self.min_speed,self.max_speed)
            boosted_speed = int(1.5 * base_speed)

            #crash
            if boosted_speed < dist:
                self.position += boosted_speed
                return f"{self.name} uses Nitro Boost and moves {boosted_speed} units!"
            elif boosted_speed == dist:
                self.position += dist - 1
                return f"{self.name} uses Nitro Boost and stops before an obstacle!"  
        else: 
            return f"{self.name} does not have enough energy to use Nitro Boost."
        