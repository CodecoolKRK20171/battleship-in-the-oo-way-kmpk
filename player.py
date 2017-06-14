# from ocean import Ocean
# from ship import Ship
from random import randint


class Player:

    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def shoot_on_board_player(self, board, position):
        letters = {'A': 2, 'B': 3, 'C': 4, 'D': 5, 'E': 6, 'F': 7, 'G': 8, 'H': 9, 'I': 10, 'J': 11}

        if board.board[int(position[1])][letters[position[0]]].is_ship:
            board.board[int(position[1])][letters[position[0]]].mark()
        else:
            board.board[int(position[1])][letters[position[0]]].show()

    def shoot_on_board_ai(self, board):
        position_x = randint(2, 11)
        position_y = randint(0, 9)

        print(position_x,position_y)

        if board.board[position_y][position_x].is_ship:
            board.board[position_y][position_x].mark()

        else:
            board.board[position_y][position_x].show()

    def is_alive(self, board):
        available_square_ship = 0
        for row in board:
            for column in row:
                if board.board[row][column].is_ship:
                    available_square_ship += 1
        if available_square_ship == 0:
            return False
        else:
            return True
