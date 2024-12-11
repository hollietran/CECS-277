from plate import Plate

class PlateDecorator(Plate):  # Inherit only from Plate
    def __init__(self, plate):
        self._plate = plate

    def description(self):
        return self._plate.description()

    def area(self):
        return self._plate.area()

    def weight(self):
        return self._plate.weight()

    def count(self):
        return self._plate.count()
