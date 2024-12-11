from plate import Plate

class SmallPlate(Plate):
    def __init__(self):
        self._description = "Sturdy 10-inch paper plate with"
        self._area = 78
        self._weight = 32

    def description(self):
        return self._description

    def area(self):
        return self._area

    def weight(self):
        return self._weight

    def count(self):
        return 0