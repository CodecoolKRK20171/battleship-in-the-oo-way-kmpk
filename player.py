from ocean import Ocean
from ship import Ship


class Player:

    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def shoot_on_board(self, board, x, y):
        if board[y][x].is_ship = True:
            board[y][x].mark()

        return board

    def is_alive(self, board):
        available_square_ship = 0
        for row in board:
            for column in row:
                if board[row][column].is_ship = True:
                    available_square_ship += 1
        if available_square_ship = 0:
            return False
        else:
            return True
