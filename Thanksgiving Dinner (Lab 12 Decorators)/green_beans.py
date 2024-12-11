from plate_decorator import PlateDecorator

class GreenBeans(PlateDecorator):
    def __init__(self, plate):
        super().__init__(plate)

    def description(self):
        return super().description() + " GreenBeans and"

    def area(self):
        return self._plate.area() - 20

    def weight(self):
        return self._plate.weight() - 3

    def count(self):
        return self._plate.count() + 1
