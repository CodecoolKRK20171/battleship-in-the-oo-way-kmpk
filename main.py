from ocean import Ocean
from player import Player
from os import system
import csv


def read_ascii():

    with open('ship.csv', 'r') as f:
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
    # kreacja startowego boardu
    board_1 = Ocean(player_1)
    board_2 = Ocean(player_2)
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


def ask_for_name():
    name = input("\nAhoy! Wha' be yer name?\n")
    return name


def check_end_game(player_1, player_2):
    if not player_1.is_alive:
        show_lose_screen()
    if not player_2.is_alive:
        show_win_screen()


def print_boards(board_1, board_2):
    #
    print(board_1)
    #
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


def main():

    board1, board2, player1, player2 = create_game()
    while True:
        system("clear")
        print_boards(board1, board2)
        # jakieś komunikaty, pytanie o pozycje
        target = ask_for_positions()
        shoot = player1.shoot_on_board_player(board2, target)
        # jakiś komunikat
        shoot = player2.shoot_on_board_ai(board1)
        # jakiś komunikat
        check_end_game(player1, player2)


def show_lose_screen():
    pass


if __name__ == "__main__":
    main()
