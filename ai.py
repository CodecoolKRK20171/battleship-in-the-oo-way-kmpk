from ocean import Ocean
from random import randint

class AI:
    def __init__(self):
        self.marked = []
        self.unmarked = []

    def shoot_on_board_ai(self, board):
        position_x = randint(2, 11)
        position_y = randint(0, 9)

        print(position_x,position_y)

        if board.board[position_y][position_x].is_ship:
            board.board[position_y][position_x].mark()
            self.marked.append(board.board[position_y][position_x])

        else:
            self.unmarked.append(board.board[position_y][position_x])
            print(board.board[position_y][position_x])
            board.board[position_y][position_x].show()
