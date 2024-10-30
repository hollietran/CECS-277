import random
from hero import Hero
from map import Map
from enemy import Enemy
from check_input import get_int_range

def main():
    # prompt the user to enter name:
    name = input("What is your name, traveler? ") 
    
    # construct the hero and a map object:
    hero = Hero(name)
    dungeon_map = Map()
    # The first call to show_map should display the hero at the top-left corner (0, 0)
    print(dungeon_map.show_map((hero.row, hero.col)))
    
    # Loop that repeats until the hero dies
    while True:

        # Present a menu that allows the user to choose a direction to move
        print("\n1. Go North")
        print("2. Go South")
        print("3. Go East")
        print("4. Go west")
        print("5. Quit")
        choice = get_int_range("Enter Choice: ", 1, 5)

        if choice == 5:
            print("Thanks for playing")
            break

        # Move the hero in that direction
        if choice == 1:
            result = hero.go_north(dungeon_map)
        elif choice == 2:
            result = hero.go_south(dungeon_map)
        elif choice == 3:
            result = hero.go_east(dungeon_map)
        elif choice == 4:
            result = hero.go_west(dungeon_map)
        
         # o = invalid direction
        if result == 'o':
            # Display a message stating that they cannot move that direction
            print("You cannot go that way...")

        # Reaveal that spot
        current_loc = (hero.row, hero.col)
        dungeon_map.reveal(current_loc)
        print(dungeon_map.show_map(current_loc))

        # Present the encounter at that location as follows:
        # m = monster
        if result == 'm':
            enemy = Enemy()
            print(f'You encounter a {enemy.name} with HP: {enemy.hp}/{enemy._max_hp}')

            # Loop that allows the user to either attack or run away
            while enemy.hp > 0:
                # if attack, and monster dont die, monster attacks back
                print("\n1. Attack")
                print("2. Run Away")
                action = get_int_range("Enter Choice: ", 1, 2)

                if action == 1:
                    print(hero.attack(enemy))
                    # if monster dies, then display a message and remove the 'm' from the map
                    if enemy.hp > 0:
                        print(enemy.attack(hero))
                    else:
                        print(f"You have slain the {enemy.name}")
                    
                    current_loc = (hero.row, hero.col)
                    dungeon_map.reveal(current_loc)
                    print(dungeon_map.show_map(current_loc))

                # if run away, then choose random direction to run in
                elif action == 2:
                    direction = random.randint(1,4)
                    if direction == 1:
                        hero.go_north(dungeon_map)
                    elif choice == 2:
                        result = hero.go_south(dungeon_map)
                    elif choice == 3:
                        result = hero.go_east(dungeon_map)
                    elif choice == 4:
                        result = hero.go_west(dungeon_map)
                    dungeon_map.reveal((hero.row, hero.col))
                    
                    # (reveal but don't present the encounter for the new location)
                    new_loc = (hero.row, hero.col)
                    dungeon_map.reveal(new_loc)
                    print("You ran away!")
                    print(dungeon_map.show_map(new_loc))
                    break
                    # 'm' remains in map

        # n = nothing
        elif result == 'n':
            # Display that this is an empty room
            print("There is nothing here...")
        
        # s = start
        elif result == 's':
            # Display a message that they wound up back at the start of the dungeon
            print("You are back at the start of the dungeon.")

        # i = item room
        elif result == 'i':
            # Display a message that they found a health potion.
            print("You found a Health Potion! You drink it to restore you health.")
            hero.heal()
            dungeon_map.remove_at_loc(current_loc)
            # Heal the hero and remove the 'i' from the map so they can't get it again
            # Not required, however you can check if hero's hp is full, leave 'i' on map for later

        # f = finish
        elif result == 'f' or (hero.row==4 and hero.col==4):
            # Display message that they found the way out of the maze and won the game.
            print("Congratulations! You have found the exit and escaped the dungeon!")
            break
    
        if hero.hp <= 0:
            print("You have been defeated by the monsters in the dungeon.")
            break

        print(hero)

if __name__ == '__main__':
    main()