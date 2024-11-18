from easy_door_factory import EasyDoorFactory
from difficult_door_factory import DifficultDoorFactory
from check_input import get_int_range

def open_door(door):
    # Prints the current condition of door
    print(door.examine_door())

    choice = get_int_range(door.menu_options(), 1, door.get_menu_max())
    print(door.attempt(choice))

    # Loop that repeats until the door is unlocked
    while not door.is_unlocked():
        print(door.clue())
        
        # Gets the player's choice from door's menu options
        choice = get_int_range(door.menu_options(), 1, door.get_menu_max())

        # prints the attempt that took place
        print(door.attempt(choice))

    # checks if the attempt is successful or not
    print(door.success())

def main():
    print("Welcome to the Escape Room. You must unlock 3 doors to escape...")

    difficulty = get_int_range("Enter Difficulty (1. Easy 2. Hard): ", 1,2)
    
    if difficulty == 1:
        factory = EasyDoorFactory()
    else:
        factory = DifficultDoorFactory()
    
    num = 0
    while num < 3:
        door = factory.create_door()
        open_door(door)
        num += 1
    
    print("Congratulations! You escaped... this time.\n")

main()