from ocean import Ocean
from player import Player
from ship import Ship
from os import system
import csv


def read_ascii(file_name):

    with open(file_name, 'r') as f:
        r = csv.reader(f)
        for row in r:
            print("".join(row))


def create_game():

    system("clear")
    read_ascii()
    determine_number_of_players()
    player_name = ask_for_name()
    player_1 = Player(player_name)
    player_2 = Player("AI")
    board_1 = Ocean(player_1)
    board_2 = Ocean(player_2)
    while Ship.ships:
        name = add_ships(board_2)
        del Ship.ships[name]
    board_1.fill_board()
    board_2.fill_board()

    return board_1, board_2, player_1, player_2


def determine_number_of_players():
    print("\nMornin' cap'n! How many players will battle? ")
    while True:
        game_mode = input("\n'1' for singleplayer, '2' for multiplayer\n")
        if game_mode == "1":
            break
        else:
            print("\n Dammit! Unsupported game mode :(\n")
    return game_mode


def add_ships(board):
    pos_x = int(input('Enter new ship X position: '))
    while pos_x not in range(1, 11):
        pos_x = int(input('Please enter a correct X position: '))
    pos_y = int(input('Enter new ship Y position: '))
    while pos_y not in range(1, 11):
        pos_y = int(input('Please enter a correct Y position: '))

    start_position = (pos_x, pos_y)

    horizontal = input('Do you want the ship to be placed horizontallyt? (y/n): ')
    while horizontal not in 'yn':
        horizontal = input('Please enter the right option: ')

    if horizontal == 'y':
        horizontal = True
    else:
        horizontal = False

    name = input('Choose the ship kind (Carrier, Battleship, Cruiser): ')
    while name not in Ship.ships.keys():
        name = input('Enter the right ship name: ')

    ship1 = Ship(start_position, horizontal, name)
    board.ships.append(ship1)

    return name


def ask_for_name():
    name = input("\nAhoy! Wha' be yer name?\n")
    return name


def check_end_game(player_1, player_2):
    if not player_1.is_alive:
        read_ascii('lose_screen.csv')
    if not player_2.is_alive:
        read_ascii('win.csv')


def print_boards(board_1, board_2):

    colors = {"blue": "\033[1;34m",
              "yellow": "\033[1;33m",
              "reset": "\033[0;0m"}

    print(colors["yellow"] + "  * * * YOUR BOARD * * *  \n" + colors["reset"])
    print(board_1)
    print(colors["yellow"] + " * * * ENEMY BOARD * * *  \n" + colors["reset"])
    print(board_2)


def ask_for_positions():

    error_msg = "\nYo! Enter correct co-ordinates mate...\n"
    while True:
        target = input("Where do ye wants t' shoot? (eg. a1)\n")

        try:
            row, column = target[0].upper(), int(target[1])
        except IndexError:
            print(error_msg)
        except ValueError:
            print(error_msg)
        else:
            if len(target) == 2 and row in "ABCDEFGHIJ" and column in range(0, 10):
                target = row.upper() + str(column)
                break
            else:
                print(error_msg)
    return target


def handle_shooting_phase(board_1, board_2, player_1, player_2):
    target = ask_for_positions()
    player_1.shoot_on_board_player(board_2, target)
    player_2.shoot_on_board_ai(board_1)


def main():

    board_1, board_2, player_1, player_2 = create_game()
    while True:
        system("clear")
        print_boards(board_1, board_2)
        handle_shooting_phase(board_1, board_2, player_1, player_2)
        check_end_game(player_1, player_2)


if __name__ == "__main__":
    main()
