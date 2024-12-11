from plate import Plate

class LargePlate(Plate):
    def __init__(self):
        self._description = "Flimsy 12-inch paper plate with"
        self._area = 113
        self._weight = 24

    def description(self):
        return self._description

    def area(self):
        return self._area

    def weight(self):
        return self._weight

    def count(self):
        return 0
