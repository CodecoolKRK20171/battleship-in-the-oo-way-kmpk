from ocean import Ocean
from random import randint


class AI:

    def __init__(self, difficulty="medium"):
        self.marked = []
        self.unmarked = []
        self.shooted_target = []
        self.difficulty = difficulty

    def shoot_on_board_ai(self, battlefield):

        if self.difficulty == "easy":
            self.shooted_target = []

        position_x = randint(0, 9)
        position_y = randint(0, 9)
        target = battlefield.board[position_y][position_x]

        while target in self.shooted_target:
            position_x = randint(0, 9)
            position_y = randint(0, 9)
            target = battlefield.board[position_y][position_x]

        self.shooted_target.append(target)

        if target.is_ship:
            target.mark()
            self.marked.append(target)

        else:
            self.unmarked.append(target)
            target.make_border()

        return (position_x, position_y)

    @classmethod
    def set_difficulty(cls, mode):

        cls.difficulty = mode
