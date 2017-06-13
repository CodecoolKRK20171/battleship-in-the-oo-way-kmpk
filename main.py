from ocean import Ocean
from player import Player


def create_game():
    # pytaj o ilość graczy
    # pytaj o imię
    player1 = Player("Gracz")
    player2 = Player("AI")
    # kreacja startowego boardu
    board1 = Ocean(player1)
    board2 = Ocean(player2)

    return board1, board2, player1, player2


def check_end_game(player1, player2):
    if not player1.is_alive:
        show_lose_screen()
    if not player2.is_alive:
        show_win_screen()


def print_boards(board1, board2):
    # board1.fill_board()
    print(board1)
    # board2.fill_board()
    print(board2)


def ask_for_positions():
    x = input("X ")
    y = input("Y ")
    return int(x), int(y)


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
