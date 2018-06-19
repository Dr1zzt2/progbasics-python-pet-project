import sys
import time


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
