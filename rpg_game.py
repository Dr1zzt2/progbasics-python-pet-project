import sys
import time
import main
import pickle
import rpg_inventory
from random import randint


def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.1)


def start_game():
    print_slow("Greetings!\n")
    time.sleep(1)
    print_slow("You are a prisoner thrown into a very ancient dungeon.\n")
    time.sleep(1)
    print_slow("You have no objectives. Trying to escape is absolutely futile.\n")
    time.sleep(1)
    print_slow("It's time to choose your class.\n")
    time.sleep(1)
    game_core(False)


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


def choose_kit():
    pass


def game_core(save_state):
    options = ["1. Move",
               "2. Check Status",
               "3. Inventory",
               "4. Save Game",
               "5. Quit to Menu"]
    if save_state is False:
        player_class = pick_class()
        dungeon = create_dungeon()
        start_position = find_start_position(dungeon)
        current_position = start_position
    if save_state is True:
        current_position, dungeon, player_class = game_load()
    while True:
        for option in options:
            print(option)
        option = input("Please enter a number: ")
        if option == "1":
            current_position = movement(dungeon, current_position)
            encounter(dungeon, current_position)
        elif option == "2":
            check_status()
        elif option == "3":
            game_save(current_position, dungeon, player_class)
            rpg_inventory.show_inv_menu()
        elif option == "4":
            game_save(current_position, dungeon, player_class)
        elif option == "5":
            main.main()
        else:
            print("There is no such option.")


def encounter(dungeon, current_position):
    with open("dungeon_descriptions.txt", "r") as descriptions_file:
        description_list = descriptions_file.readlines()
    print("You are in" + description_list[dungeon[current_position[0]][current_position[1]]][4:])


def find_start_position(dungeon):
    for y in dungeon:
        if 1 in y:
            start_position = [y.index(1), dungeon.index(y)]
    return start_position


def movement(dungeon, current_position):
    options = []
    battle_random = randint(1, 10)
    if current_position[1] > 0:
        options.append("N: North")
    if current_position[0] > 0:
        options.append("W: West")
    if current_position[0] < 5:
        options.append("E: East")
    if current_position[1] < 5:
        options.append("S: South")
    while True:
        for option in options:
            print(option)
        option = input("Please enter a letter: ")
        if option == "n" and "N: North" in options:
            current_position[1] -= 1
            if battle_random == 1 or 3 or 9:
                battle()
            return current_position
        elif option == "w" and "W: West" in options:
            current_position[0] -= 1
            return current_position
        elif option == "e" and "E: East" in options:
            current_position[0] += 1
            return current_position
        elif option == "s" and "S: South" in options:
            current_position[1] += 1
            return current_position
        else:
            print("There is no such option.")


def check_status():
    pass


def heroes_hp():
    heroes_hp_stat = {'Warrior': 100, 'Ranger': 80, 'Mage': 60}
    return heroes_hp_stat


def heroes_dmg():
    heroes_dmg_stat = {'Warrior': 30, 'Ranger': 40, 'Mage': 50}
    return heroes_dmg_stat


def load_hero_stat(hp, dmg, pick_class):
    if pick_class == "Warrior":
        return heroes_stat['Warrior']
    elif pick_class == "Ranger":
        return heroes_stat['Ranger']
    elif pick_class == "Mage":
        return heroes_stat['Mage']


def create_dungeon():
    dungeon = [[0 for x in range(6)] for y in range(6)]
    while True:
        x = randint(0, 5)
        y = randint(0, 5)
        room = randint(0, 36)
        room_reserved_check = False
        for y_pos in dungeon:
            if room in y_pos:
                room_reserved_check = True
        if dungeon[x][y] == 0 and room_reserved_check is False:
            dungeon[x][y] = room
        full_check = True
        for y_pos in dungeon:
            if 0 in y_pos:
                full_check = False
        if full_check is True:
            break
    return dungeon


def game_save(current_position, dungeon, player_class):
    with open('savefile.dat', 'wb') as f:
        pickle.dump([current_position, dungeon, player_class], f)
    print("Game Saved!")


def game_load():
    with open('savefile.dat', 'rb') as f:
        current_position, dungeon, player_class = pickle.load(f)
    print(current_position, dungeon, player_class)
    print("Game Loaded!")
    return current_position, dungeon, player_class


def monster_choose(filename):
    with open(filename, "r") as f:
        lines = [line.split("\t")[0] for line in f]
    random_get = randint(1, 12)
    return lines[random_get]


def health_check(health, name):
    if health <= 0:
        print(str(name) + ' died\n')
        return True


def battle():
    heroes = heroes_stat()
    with open('monsters.txt') as f:
        Monster_hp = [line.split('\t')[1] for line in f]
    with open('monsters.txt') as f:
        Monster = [line.split('\t')[0] for line in f]
    random_monster = randint(1, 12)
    which_monster = Monster[random_monster]
    hero_health = 100
    monster_health = Monster_hp[random_monster]
    print_slow('You have encountered ' + str(Monster[random_monster]) + ' get ready for battle!\n')
    print_slow(which_monster + 's health: ' + monster_health + '\n')
    while True:
        if health_check(hero_health, "Hero") is True:
            break
        input('Attack brave Hero\n')
        print(str(hero_health) + ' hp\n')
        hero_dmg = randint(10, 30)
        monster_health = int(monster_health) - hero_dmg
        print('The Hero attacked the Monster for ' + str(hero_dmg) + ' damage\n')
        if health_check(monster_health, which_monster) is True:
            break
        print('The monster has ' + str(monster_health) + ' hp left\n')
        print("-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+\n")
        input("Monster's turn")
        print('Monster attack\n')
        print(str(monster_health) + ' hp\n')
        monster_dmg = randint(10, 20)
        hero_health = hero_health - monster_dmg
        print('The Monster attacked the Hero for ' + str(monster_dmg) + ' damage\n')
        print('The Hero has ' + str(hero_health) + ' hp left\n')
        print("-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+\n")
