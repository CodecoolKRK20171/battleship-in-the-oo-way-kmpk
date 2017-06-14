# from ocean import Ocean
# from ship import Ship
from ai import AI
import common


class Player:

    def __init__(self, name):

        self.name = name
        self.is_alive = True

    def shoot_on_board_player(self, battlefield, coords):

        pos_y, pos_x = common.convert_coords(coords)
        target = battlefield.board[pos_x][pos_y]
        print(pos_x, pos_y)
        print(target.__dict__)

        if target.is_ship:
            target.mark()
        else:
            target.show()

    def shoot_on_board_ai(self, board):

        ai = AI()
        target = ai.shoot_on_board_ai(board)
        return target

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

    def __str__(self):
        return str(self.name)
