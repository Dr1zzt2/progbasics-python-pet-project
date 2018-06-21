import rpg_game


def show_equiped_items():
    pass


def show_items(inventory):
    with open(inventory) as f:
        for line in f:
            for word in line.split():
                print(word)
    options = ['1. Equip an item',
               '2. Back to backpack']
    print('Items \n')
    for option in options:
        print(option)
    while True:
        option = input('Please enter a number: \n')
        if option == '1':
            pass
        elif option == '2':
            show_inv_menu()


def show_inv_menu():
    options = ['1. Equiped item(s)',
               '2. Backpack',
               '0. Exit']
    print("Inventory: \n")
    for option in options:
        print(option)

    while True:
        options = input('Please enter a number: \n')
        if options == '1':
            show_equiped_items()
        elif options == '2':
            display_inventory('inventory.txt')
        elif options == '0':
            rpg_game.game_core(rpg_game.game_load())


def display_inventory(inventory):
    print("Inventory:")
    for k, v in inventory.items():
        print(k, v)
    print("Total number of items:", sum(inventory.values()))
