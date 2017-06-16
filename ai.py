from ocean import Ocean
from random import randint


class AI:
    """Class responsible for the second player shooting"""

    shooted_target = []
    difficulty = "medium"

    def __init__(self):
        """Initialize function. Createas attributes needed for AI.

        Args:
            none

        Returns:
            none

        """

        self.marked = []
        self.unmarked = []

    def shoot_on_board_ai(self, battlefield):

        if self.difficulty == "easy":
            self.shooted_target = []

        """AI shooting function.

        Args:
            battlefield: Playable area. List of lists of square objects.

        Returns:
            position_x: X coordinate of the shoot made by AI.
            position_y: Y coordinate of the shoot made by AI.

        """
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
