from square import Square


class Ocean:

    def __init__(self):
        """Initialize function. Responsible for handling the playable area.

        Args:
            self: Object carrying attribute.
            position: Position of a newly made ship.

        Returns:
            none

        """
        self.ships = []
        self.board = []

    def fill_board(self):
        """Fills the board with Square objects.

        Args:
            self: Object carrying attribute.

        Returns:
            none

        """
        for i in range(0, 10):
            for j in range(0, 10):
                self.board.append(Square(i, j))

    def __str__(self):
        """Prints out the ocean object.

        Args:
            self: Object carrying attribute:

        Returns:
            ocean: The playable area.

        """
        ocean = ''
        ocean += '    ABCDEFGHIJ \n'
        ocean += '   ' + '-' * 12 + '\n'
        ocean += '1  |'
        for i in range(len(self.board)):
            if i % 10 == 0 and i != 0:
                ocean += '|\n' + '{0:{width}}|'.format(str(int((i + 10)/10)), width=3)
            ocean += str(self.board[i])
        ocean += '|\n'
        ocean += '   ' + '-'*12

        return ocean
