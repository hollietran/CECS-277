from abc import ABC, abstractmethod

class Plate(ABC):
    @abstractmethod
    def description(self): #returns the description of the plate
        pass

    @abstractmethod
    def area(self): # returns the area of plate
        pass

    @abstractmethod
    def weight(self):# returns the weight limit of the plate
        pass

    @abstractmethod
    def count(self): # return the count of items on plate.
        pass
