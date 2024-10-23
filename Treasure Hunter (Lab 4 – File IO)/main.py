#Name: Min, Hollie
#Discriptions: This program is a treasure hunting game. The user will be given a map with traps and 7 treasures hidden in a 7x7 matrix, The player will move around the map using WASD keys, and by collecting all 7 treasure the player will win. However, upon touching a trap, the player will lose instantly and will be show their score. By adding a look around function, the player can see the surrounding area of the map, and can see if there is a trap nearby which adds a similar feel of minesweeper.

def read_map():
    """Reads the map from the file and stores the contents in a 7x7 2D list. 
    Each character in the maze (after removing spaces and new lines) 
    should be stored as a separate element in the 2D list."""
    with open("map.txt", "r") as map_file:
        map_list = [list(line.replace(" ", "").strip()) for line in map_file if line.strip()]
    return map_list


def display_map(map, player):
    """Displays the map with the player's position marked as 'P'."""
    for row in range(len(map)):
        for col in range(len(map[row])):
            if row == player[0] and col == player[1]:
                print(" P", end="")
            else:
                print(map[row][col], end="")
        print()

def move_player(player, direction, upper_bound):
    """Moves the player in the selected direction (W=up, A=left, S=down, D=right). Checks for boundaries."""
    row, col = player
    if direction == 'W' and row > 0:  # Move Up
        player[0] -= 1
    elif direction == 'A' and col > 0:  # Move Left
        player[1] -= 1
    elif direction == 'S' and row < upper_bound[0] - 1:  # Move Down
        player[0] += 1
    elif direction == 'D' and col < upper_bound[1] - 1:  # Move Right
        player[1] += 1
    else:
        print("You cannot move there.")
    return player


def count_treasures_traps(map, player, upper_bound):
    """Counts the number of treasures and traps within a 1-space radius from the player's current position."""
    count_treasure = 0
    count_trap = 0
    for row in range(max(0, player[0] - 1), min(upper_bound[0], player[0] + 2)):
        for col in range(max(0, player[1] - 1), min(upper_bound[1], player[1] + 2)):
            if map[row][col] == 'T':  # Check for treasures
                count_treasure += 1
            elif map[row][col] == 'X':  # Check for traps
                count_trap += 1
    return count_treasure, count_trap

def main():
    map = read_map()  # Load the hidden map
    
    player = [0, 0]  # Set initial player position
    upper_bound = [len(map), len(map[0])]  # Set the boundaries based on map size
    user_map = [[' .' for _ in range(len(map[0]))] for _ in range(len(map))]  # Create a blank map for the user
    game_over = False
    score = 0
    treasure_remaining = sum(row.count('T') for row in map)
    treasure_found = []

    print("Treasure Hunt!\nFind the treasures without getting caught in a trap.")
    # Loop to keep game running
    while not game_over:
        display_map(user_map, player)
        direction = input("Enter Direction (WSAD or L to Look around or Q to quit) : ").upper()

        if direction == 'Q':
            print("You've quit the game.")
            break

        elif direction == 'L':
            print("You look around.")
            treasure, trap = count_treasures_traps(map, player, upper_bound)
            print(f"You found {treasure} treasure(s) and {trap} trap(s) nearby.")
            user_map[player[0]][player[1]] = ' ' + str(trap)

        elif direction in ['W', 'A', 'S', 'D']:
            move_player(player, direction, upper_bound)
            if 0 <= player[0] < 7 and 0 <= player[1] < 7:  # Check if the player is within map boundaries
                current_cell = map[player[0]][player[1]]

                if current_cell == 'T':
                    if (player[0], player[1]) not in treasure_found:  # Check if the treasure is already found
                        treasure_found.append((player[0], player[1]))  # Add to the treasure found list if new
                        user_map[player[0]][player[1]] = " T"  # Update the user map with the treasure symbol
                        score += 1
                        print(f"You found {score} treasure!")
                        treasure_remaining -= 1
                        if treasure_remaining == 0:
                            print("Congratulations! You've found all the treasures!")
                            game_over = True

                elif current_cell == 'X':
                    print("You fell into a trap!")
                    print(f"You found {score} treasure(s)!")
                    print("Game Over!")
                    game_over = True
                else:
                    print(f"You moved {direction}.")
            else:
                print("You cannot move outside the map boundaries.")

        else:
            print("Invalid input, please enter W, A, S, D, L, or Q.")

main()
