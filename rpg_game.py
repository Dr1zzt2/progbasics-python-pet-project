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
    pick_class()
