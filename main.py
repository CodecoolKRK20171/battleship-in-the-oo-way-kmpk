from ocean import Ocean
from player import Player


def create_game():

    determine_number_of_players()
    player_name = ask_for_name()
    player_1 = Player(player_name)
    player_2 = Player("AI")
    # kreacja startowego boardu
    board_1 = Ocean(player_1)
    board_2 = Ocean(player_2)

    return board_1, board_2, player_1, player_2


def determine_number_of_players():
    print("Mornin' cap'n! How many players will battle? ")
    while True:
        game_mode = input("'1' for singleplayer, '2' for multiplayer ")
        if game_mode == "1":
            break
        else:
            print("Dammit! Unsupported game mode :(")


def ask_for_name():
    name = input("Ahoy! Wha' be yer name?")
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

    error_msg = "Yo! Enter correct co-ordinates mate..."
    while True:
        target = input("Where do ye wants t' shoot? (eg. a1)")

        try:
            row, column = target[0], int(target[1])
        except IndexError:
            print(error_msg)
        except ValueError:
            print(error_msg)
        else:
            print(target, len(target), row in "abcdefghij", column in range(0, 10))
            if len(target) == 2 and row in "abcdefghij" and column in range(0, 10):
                break
            else:
                print(error_msg)

    return target


def main():
    board1, board2, player1, player2 = create_game()
    board1.fill_board()
    board2.fill_board()
    while True:
        print_boards(board1, board2)
        # jakieś komunikaty, pytanie o pozycje
        x, y = ask_for_positions()
        shoot = player1.shoot_on_board(board2, x, y)
        # jakiś komunikat
        x, y = ask_for_positions()
        shoot = player2.shoot_on_board(board1, x, y)
        # jakiś komunikat
        check_end_game(player1, player2)


def show_lose_screen():
    pass


def show_win_screen():
    pass


if __name__ == "__main__":
    main()
