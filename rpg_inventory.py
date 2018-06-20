def show_equiped_items():
    pass


def show_items(inventroy):
        print(inventroy.readlines())


def show_inv_menu():
    options = ['1. Equiped item(s)',
               '2. Backpack']

    while True:
        if options == '1':
            show_equiped_items()
        elif options == '2':
            show_items('inventory.txt')
        elif options == '0':
            exit()
