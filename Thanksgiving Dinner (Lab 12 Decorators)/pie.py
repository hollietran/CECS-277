from plate_decorator import PlateDecorator

class Pie(PlateDecorator):
    def __init__(self, plate):
        super().__init__(plate)

    def description(self):
        return super().description() + " Pie and"

    def area(self):
        return super().area() - 19

    def weight(self):
        return super().weight() - 8

    def count(self):
        return super().count() + 1
