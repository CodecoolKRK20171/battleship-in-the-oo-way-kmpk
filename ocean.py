from square import Square


class Ocean:

    def __init__(self, position):
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
            self.board.append(temp_list)

        self.board2 = self.board[:]
        index = 0

        for row in self.board2:

            row.insert(0, index)
            row.insert(1, '║')
            row.append('║')
            index += 1

    def __str__(self):
        """Prints out the ocean object.

        Args:
            self: Object carrying attribute:

        Returns:
            ocean: The playable area.

        """
        board_lenght = 12
        ocean = ''
        index = 0
        ocean += '  ║ A B C D E F G H I J ║\n'
        ocean += '══╬' + '══' * (board_lenght-2) + '═╣\n'

        for row in self.board2:
            for square in row:
                ocean += str(square) + " "
            ocean += '\n'
        ocean += '══╩' + '══' * (board_lenght-2) + '═╝\n'

        return ocean
