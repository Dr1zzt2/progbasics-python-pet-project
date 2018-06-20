import sys
import time
import main
import pickle
import rpg_inventory


def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.1)


def start_game():
    print_slow("Welcome!\n")
    time.sleep(1)
    print_slow("You are a prisoner thrown into a very ancient dungeon.\n")
    time.sleep(1)
    print_slow("You have no objectives. You will never escape the pit.\n")
    time.sleep(1)
    print_slow("It's time to choose your class.\n")
    time.sleep(1)
    player_class = pick_class()
    game_core()


def pick_class():
    options = ["1. Warrior",
               "2. Ranger",
               "3. Mage"]
    print("Classes:")
    for option in options:
        print(option)
    while True:
        option = input("Please enter a number: ")
        if option == "1":
            print_slow("So, you are a Warrior eh?\n")
            time.sleep(1)
            print_slow("Do you think it's smart butting your head into the wall?\n")
            return "Warrior"
        elif option == "2":
            print_slow("You have chosen Ranger.\n")
            time.sleep(1)
            print_slow("Your bow won't save you here.\n")
            return "Ranger"
        elif option == "3":
            print_slow("Mage...\n")
            time.sleep(1)
            print_slow("But do you know any spells?\n")
            return "Mage"
        else:
            print("There is no such class.")


def game_core():
    options = ["1. Move",
               "2. Check Status",
               "3. Save Game"
               "4. Quit to Menu"]
    create_map()
    while True:
        print(check_position())
        option = input("Please enter a number: ")
        if option == "1":
            movement()
        elif option == "2":
            check_status()
        elif option == "3":
            rpg_inventory.show_inv_menu()
        elif option == "4":
            main.main()
        else:
            print("There is no such option.")


def check_position():
    pass


def create_dungeon():
    pass


def game_save(data):
    with open('savefile', 'w') as f:
        pickle.dump(data, f)
