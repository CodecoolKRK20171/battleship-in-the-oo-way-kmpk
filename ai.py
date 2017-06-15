from ocean import Ocean
from random import randint


class AI:
    def __init__(self):
        self.marked = []
        self.unmarked = []

    def shoot_on_board_ai(self, battlefield):
        position_x = randint(0, 9)
        position_y = randint(0, 9)

        # print(position_x, position_y)
        target = battlefield.board[position_y][position_x]

        if target.is_ship:
            target.mark()
            self.marked.append(target)

        else:
            self.unmarked.append(target)
            # print(target)
            target.make_border()

        return (position_x, position_y)
