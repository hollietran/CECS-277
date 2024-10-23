from abc import abstractmethod
import random

class Vehicle():
    def __init__(self, name, initial, min_speed, max_speed):
        # set the attributes using the parameters
        self.name = name
        self.initial = initial
        self.min_speed = min_speed
        self.max_speed = max_speed

        # assign 0 to position and 100 to energy
        self.position = 0
        self.energy = 100

        #Differentiate between player and Bots
        self.is_player = False
        self.lane = 0
        self.prev_pos = []

    def fast(self, dist):
        # dist == distance between vehical and next obstacle
        # if energy >= 5, randomize a value between min and max_speed for the amount of spaces to move, -5 energy
        if self.energy < 5:
            return f"{self.name} doesn't have enough energy to go fast."
        
        movement = random.randint(self.min_speed, self.max_speed)
        self.energy -= 5

        # if movement == position of obstacle, crash and stop at obstacle
        if movement >= dist:
            self.position += dist
            return f"{self.name} crashed into the obstacle at position {self.position}."
        else:
            self.position += movement
            
        # Return string that describes the event that occured
        return f"{self.name} moved {movement} spaces and is now at position {self.position}. Remaining energy: {self.energy}"
    
    def slow(self, dist):
        # dist == distance between vehical and next obstacle
        # the vehicle moves at half speed, no energy cost
        movement = random.randint(self.min_speed, self.max_speed) // 2
        self.position += movement

        # if there is an obstacle, then it will go around it
        if self.position == dist:
            self.position = dist + 1
            return f"{self.name} avoided the obstacle at position {dist} and moved to position {self.position}"
        
        # returns a string that describes the event that occured
        return f"{self.name} moved slowly {movement} spaces and is now at position {self.position}"

    def __str__(self):
        # returns a string with the vehicl's name, position and energy
        return f"{self.name}, {self.position}, {self.energy}"

    @abstractmethod
    def description_string(self):
        # A string to describe the vehicle.
        pass

    @abstractmethod
    def special_move(self, dist):
        # Special move specific to each vehicle
        pass