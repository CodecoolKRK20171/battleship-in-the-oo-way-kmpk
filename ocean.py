from square import Square


class Ocean:

<<<<<<< HEAD
    def __init__(self, owner):
=======
    def __init__(self):
        """Initialize function. Responsible for handling the playable area.

        Args:
            self: Object carrying attribute.
            position: Position of a newly made ship.

        Returns:
            none

        """
>>>>>>> 50fa51be90e2c49406c3b81d0d6be2ac830c1473
        self.ships = []
        self.board = []
        self.owner = owner

    def fill_board(self):
<<<<<<< HEAD
=======
        """Fills the board with Square objects.

        Args:
            self: Object carrying attribute.

        Returns:
            none

        """
>>>>>>> 50fa51be90e2c49406c3b81d0d6be2ac830c1473
        for i in range(0, 10):
            temp_list = []
            for j in range(0, 10):
                temp_list.append(Square(i, j))
            temp_list.append("\n")
            self.board.append(temp_list)

    def __str__(self):
<<<<<<< HEAD
        squares = ''

        for square in self.board:
            for square2 in square:
                squares += str(square2)

        return squares
=======
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
>>>>>>> 50fa51be90e2c49406c3b81d0d6be2ac830c1473
