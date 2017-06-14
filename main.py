# Plan:
#


from ocean import Ocean
import csv
import os
import sys


def make_ship_from_csv():
    """Prints a ship from a csv file

    Args:
        none

    Returns:
        none

    """
    with open("ship.csv", 'r') as f:
        r = csv.reader(f)
        for row in r:
            print("".join(row))


def menu():
    """Prints out a menu for the user.

    Args:
        none

    Returns:
        none

    """

    os.system('clear')
    make_ship_from_csv()

    print('\nWelcome to battleships!')
    start = input('\nDo you want to start the game? (y/n): ')
    while start not in ['y', 'n']:
        start = input('\nPlease enter the right option: ')

    if start == 'y':
        handle_game()
    else:
        sys.exit()


def handle_game():
    """Functio handles battleships game.

    Args:
        board: Game board.

    Returns:
        none

    """

    os.system('clear')

    bajer = Ocean()
    bajer.fill_board()

    print(bajer)


def main():

    menu()

    handle_game()


if __name__ == '__main__':
    main()
