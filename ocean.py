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
        self.board = []
        for i in range(0, 10):
            temp_list = []
            for j in range(0, 10):
                temp_list.append(Square(i, j))
            temp_list.append("\n")
            self.board.append(temp_list)

    def __str__(self):
        """Prints out the ocean object.

        Args:
            self: Object carrying attribute:

        Returns:
            ocean: The playable area.

        """
        ocean = ''

        for row in self.board:
            ocean += '|'
            row.insert(-1, '|')
            for square in row:
                ocean += str(square)
'

        return ocean
