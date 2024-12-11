# Group Members: Min, Hollie
# Program Description:
    # A game that has the user add food to their plate without going over the weight or area limit of the plate.
    # 2 Different types of plates: small = sturdy & 10 inch, large = flimsy & 12 inch
    # Plates can be decorated with 5 types of food: Turkey, Stuffing, Potatoes, Green Beans, and Pumpkin Pie.
    # Each food have different weight (oz), area (in^2).
    # If the user goes over the area or weight limit, their food falls to the floor.
 
from small_plate import SmallPlate
from large_plate import LargePlate
from turkey import Turkey
from stuffing import Stuffing
from potatoes import Potatoes
from green_beans import GreenBeans
from pie import Pie

def examine_plate(plate):
    print(plate.description()[:-4])
    if plate.area() <= 0:
        print("Your plate isn't big enough for this much food! Your food spills over the edge.")
        return True
    if plate.weight() <= 0:
        print("Your plate is too heavy! Your food falls to the floor.")
        return True

    print("Sturdiness:", "Bending" if plate.weight() <= 6 else "Weak" if plate.weight() <= 12 else "Strong")
    print("Space available:", "A tiny bit" if plate.area() <= 20 else "Some" if plate.area() <= 40 else "Plenty")
    return False

def main():
    print("- Thanksgiving Dinner -")
    print("1. Small Sturdy Plate")
    print("2. Large Flimsy Plate")
    choice = int(input("Choose a plate: "))

    plate = SmallPlate() if choice == 1 else LargePlate()

    while True:
        print("1. Turkey\n2. Stuffing\n3. Potatoes\n4. Green Beans\n5. Pie\n6. Quit")
        choice = int(input("Choose food to add: "))

        if choice == 6:
            print(plate.description())
            print(f"Good job! You made it to the table with {plate.count()} items.\nThere was still {plate.area()} square inches left on your plate.\nYour plate could have held {plate.weight()} more ounces of food.\nDon't worry, you can always go back for more. Happy Thanksgiving!")
            break

        if choice == 1:
            plate = Turkey(plate)
        elif choice == 2:
            plate = Stuffing(plate)
        elif choice == 3:
            plate = Potatoes(plate)
        elif choice == 4:
            plate = GreenBeans(plate)
        elif choice == 5:
            plate = Pie(plate)

        if examine_plate(plate):
            break

if __name__ == "__main__":
    main()
