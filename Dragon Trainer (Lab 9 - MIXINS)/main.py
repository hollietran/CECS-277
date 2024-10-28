import check_input
import random
from hero import Hero
from fire_dragon import FireDragon
from flying_dragon import FlyingDragon
from flying_fire_dragon import FlyingFireDragon

def main():
    hero_name = input("what is your name challenger?: ")
    hero = Hero(hero_name, 50) # 50 hp

    # list of dragons
    dragons = [
        FireDragon(),
        FlyingDragon(),
        FlyingFireDragon(),
    ]

    print(f"Welcome to dragon training, {hero_name}")
    print("You must defeat 3 dragons.")

    # main game
    while len(dragons) > 0 and hero.hp > 0:
        print(f"{hero_name}: {hero.hp}/{hero._max_hp}")
        for i, dragon in enumerate(dragons):
            print(f"{i+1}. {dragon}")

        # choose dragon
        dragon_choice = check_input.get_int_range("Choose a dragon to attack: ", 1, len(dragons))
        chosen_dragon = dragons[dragon_choice-1]

        # choose weapon 
        print("Attack with: \n1. Sword (2 D6)\n2. Arrow (1 D12)")
        attack_choice = check_input.get_int_range("Enter a weapon: ", 1, 2)

        if attack_choice == 1:
            # basic atk
            print(hero.basic_attack(chosen_dragon))
        else: 
            # special atk
            print(hero.special_attack(chosen_dragon))

        # defeat dragon 
        if chosen_dragon.hp == 0:
            print(f"You have defeated {chosen_dragon.name}!")
            dragons.pop(dragon_choice-1) # removes him :3

        # dragon attack     
        if len(dragons) > 0:
            attacking_dragon = random.choice(dragons)
            if random.choice([True, False]):
                print(attacking_dragon.basic_attack(hero))
            else:
                print(attacking_dragon.special_attack(hero))

        # hero alive ?
        if hero.hp == 0:
            break

    # end game msgs
    if len(dragons) == 0:
        print(f"Congratulations, {hero_name}! You have defeated all the dragons and passed the trials!")
    elif hero.hp == 0:
        print(f"{hero_name} has been defeated. Game over.")
main()