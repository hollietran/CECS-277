"""
Rad Racer Game
Author: Min Hein, Hollie Tran
Description: A racing game where the user selects a vehicle (Car, Motorcycle, Truck) and races against opponents.
"""


import motorcycle
import truck
import car
import check_input
import random

def track_creation(lanes, length):
    # Construct a 2D list that stores the track (Should have 3 lanes, 100 units long)
    track = [["-" for i in range(length)] for i in range(lanes)]

    # Randomly place 2 obstacles in each lane, but not at the start or finish
    for lane in range(lanes):
        for _ in range(2):
            obstacle_position = random.randint(1, length - 2)
            track[lane][obstacle_position] = "O"
    
    return track

def display_track(track, vehicles):
    track_copy = [row[:] for row in track]

    for lane in track:
        for i in range(len(lane)):
            if lane[i] != "O":
                lane[i] = "-"
            
    for vehicle in vehicles:
        for prev_pos in vehicle.prev_pos:
            if prev_pos < len(track[0]):
                track_copy[vehicle.lane][prev_pos] = "*"
                
    for vehicle in vehicles:
        if vehicle.position < len(track[0]):
            track_copy[vehicle.lane][vehicle.position] = "P" if vehicle.is_player else vehicle.initial
        
    for lane in track_copy:
        print("".join(lane))

def calculate_distance_to_obstacle(vehicle, track):
    # Calculate the distance to the next obstacle from the vehicle's position.
    lane = vehicle.lane
    position = vehicle.position
    track_length = len(track[lane])

    for i in range(position + 1, track_length):
        if track[lane][i] == "O":
            return i - position
    
    return float("inf")

def main():
    track = track_creation(3, 100)
    ranking = []

    # Construct a list of 3 vehicle objects.
    vehicles = [car.Car(), motorcycle.Motorcycle(), truck.Truck()]
    vehicles[0].lane = 0
    vehicles[1].lane = 1
    vehicles[2].lane = 2

    # Display the description for each vehicles and prompt the user to play as one (the rest will become opponent)
    print("Rad Racer!")
    print("Choose a vehicle and race it down the track (Player  = 'P'). Slow down for obstacles ('O') or else you'll crash!")
    for i, vehicle in enumerate(vehicles):
        print(f'{i + 1}. {vehicle.description_string()}')

    player_choice = check_input.get_int_range("Enter 1, 2, or 3: ", 1, 3)
    player_vehicle = vehicles[player_choice - 1]
    player_vehicle.is_player = True

    for vehicle in vehicles:
        if vehicle != player_vehicle:
            vehicle.is_player = False

    # Have a loop that repeats until all three vehicles have reached the finish.
    while not all (vehicle.position >= 100 for vehicle in vehicles):
        print("")
        display_track(track, vehicles)

        print("")
        for vehicle in vehicles:
            print(f'{vehicle.name} [Position - {vehicle.position}, Energy - {vehicle.energy}]')

        # Calculate distance to next obstacle for the player vehicle
        dist = calculate_distance_to_obstacle(player_vehicle, track)

        for vehicle in vehicles:
            vehicle.prev_pos.append(vehicle.position)

        if len(vehicle.prev_pos) > 5:
            vehicle.prev_pos.pop(0)

        # Each iteration, display the track and the 3 vehicles and prompt the user to move fast, slow, or special move
        if player_vehicle.position < 100:
            print("")
            move_choice = check_input.get_int_range("Chose action (1. Fast, 2. Slow, 3. Special move): ", 1, 3)
            print ("")
            if move_choice == 1:
                print(player_vehicle.fast(dist))
            elif move_choice == 2:
                print(player_vehicle.slow(dist))
            elif move_choice == 3:
                print(player_vehicle.special_move(dist))

        # The opponents randomly choose to move (40% slow, 30% fast, 30% special move)
        for vehicle in vehicles:
            if not vehicle.is_player and vehicle.position < 100:
                move_choice = random.random()
                if move_choice < 0.4:
                    print(vehicle.slow(dist))
                    
                elif (move_choice < 0.7) or (vehicle.energy < 5):
                    print(vehicle.fast(dist))
                else:
                    print(vehicle.special_move(dist))
                    
        #Adds the ranking for vehicles in order of who finished first
        for vehicle in vehicles:
            if vehicle.position >= 100 and vehicle.name not in ranking:
                ranking.append(vehicle.name)


    print("\nRace Results:")
    print(f"1st place: {ranking[0]}")
    print(f"2nd place: {ranking[1]}")
    print(f"3rd place: {ranking[2]}")

    

    """
    Extra notes:
        Place a "P" to signify player on the track
        Place a "*" to show last position(s) of player and opponents
        Keep track of finishing placements (1st, 2nd, 3rd)
        If player finishes, skip the prompts and play out the rest of the game and then display the results.

    """
main()