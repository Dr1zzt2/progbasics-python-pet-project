import sys
import rpg-game
import rpg-inventory


def choose():
    option = input("Please enter a number: ")
    if option == "1":
        start_game()
    elif option == "2":
        pass
    elif option == "3":
        sys.exit(0)
    else:
        raise KeyError("There is no such option.")


def handle_menu():
    options = ["1. Start Game",
               "2. Load Game",
               "3. Exit"]
    print("Main Menu:")
    for option in options:
        print(option)


def main():
    handle_menu()
    choose()


if __name__ == "__main__":
    main()