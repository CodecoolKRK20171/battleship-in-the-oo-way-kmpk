# from ocean import Ocean
# from ship import Ship
from ai import AI
import common


class Player:

    def __init__(self, name):

        self.name = name
        self.is_alive = True
        self.previous_shot = "Nothing"

    def shoot_on_board_player(self, battlefield, coords):

        pos_y, pos_x = common.convert_coords(coords)
        target = battlefield.board[pos_x][pos_y]
        # print(pos_x, pos_y)
        # print(target.__dict__)

        if target.is_ship:
            target.mark()
        else:
            target.show()

    def shoot_on_board_ai(self, board):

        ai = AI()
        target = ai.shoot_on_board_ai(board)
        self.previous_shot = target
        return target

    def check_if_alive(self, board):

        for ship in board.ships:
            if not ship.sunk:
                break
        else:
            self.is_alive = False

    def __str__(self):
        return str(self.name)
