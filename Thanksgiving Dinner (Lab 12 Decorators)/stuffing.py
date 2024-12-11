from plate_decorator import PlateDecorator

class Stuffing(PlateDecorator):
    def description(self):
        return super().description() + " Stuffing and"

    def area(self):
        return super().area() - 18

    def weight(self):
        return super().weight() - 7

    def count(self):
        return super().count() + 1
