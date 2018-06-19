def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.1)


def start_game():
    print_slow("Welcome")
    time.sleep(1)

