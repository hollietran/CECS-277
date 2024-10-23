import check_input
import random
from vehicle import Vehicle
from abc import abstractmethod

class Motorcycle(Vehicle):
    def __init__(self):
        #calls the superclass’s init with values for name (“Swift Bike”), initial
        # (‘M’), min_speed (6), and max_speed (8)
        super().__init__('Speedy Motorcycle', "M", 8, 12)
        

    def slow(self, dist):
        """overridden method - passes in distance to the next obstacle (if there
is one). The motorcycle will move at 75% speed, rather than half. If there’s an obstacle,
then it will go around it. There is no energy cost. Return a string that describes the event
that occurred with the name of the motorcycle and the distance traveled (if applicable)"""
        if dist > 0:
            speed = random.randint(self.min_speed,self.max_speed*.75)
            self.position += speed
            event = f"{self.name} slows down and moves {speed} units to avoid an obstacle."
        else: 
            event = f"{self.name} encounters no obstacle and continues at normal speed."
        return event

    def description_string(self):
        return f"{self.name} - speed motorcycle ({self.min_speed}-{self.max_speed} units). Special: Wheelie (2x speed but there's a chance you'll crash)."

    def special_move(self,dist):
        """passes in distance to the next obstacle (if there is one). If
there is sufficient energy (>= 15), deduct 15 energy, then there is a 75% chance that the
motorcycle will move at 2x speed, otherwise it will crash and only move one space
forward. If it was successful but there is an obstacle, then it will crash and stops in the
space just before it, otherwise it moves the randomized distance. Return a string that
describes the event that occurred with the name of the motorcycle and the distance
traveled (if applicable)."""
        if self.energy >= 15:
            self.energy -= 15
            success = random.random() < .75

            base_speed = random.randint(self.min_speed,self.max_speed)
            boosted_speed = base_speed*2

            if success:
                if boosted_speed < dist:
                    self.position += boosted_speed
                    return f"{self.name} pops a wheelie and moves {boosted_speed} units!"
                else: 
                    self.position += dist -1
                    return f"{self.name} pops a wheelie and crashes into an obstacle!"
            else:
                self.position +=1
                return f"{self.name} pops a wheelie and falls over!"
        else: 
            return f"{self.name} does not have enough energy to pop a wheelie."
        
