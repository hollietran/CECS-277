"""
Names: Min Hein, Hollie Tran

CECS 277 – Lab 14 – State
Puppy Simulator
Using the State pattern, create a puppy simulator program that has two basic functions: to feed or
play with the puppy. The puppy will react differently to these functions based on which state it
is currently in. The puppy has three possible states: asleep, eating, or playing.
"""
from puppy import Puppy

def display_menu():
    print("What would you like to do?")
    print("1. Feed the puppy")
    print("2. Play with the puppy")
    print("3. Quit")

def main():
    print("Congratulations on your new puppy!")
    puppy = Puppy()

    while True:
        display_menu()
        try:
            choice = int(input("Enter choice (1-3): "))

            if choice == 1:
                print(puppy.give_food())
            
            elif choice == 2:
                print(puppy.throw_ball())

            elif choice == 3:
                print("Goodbye!")
                break

            else:
                print("Invalid choice, Plese select a number 1, 2, or 3.")

        except ValueError:
            print("Please enter a valid number.")
        
main()