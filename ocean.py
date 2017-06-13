from square import Square


class Ocean:

    def __init__(self):
        self.ships = []
        self.board = []

    def fill_board(self):

        for i in range(0, 10):
            for j in range(0, 10):
                self.board.append(Square(i, j))

    def __str__(self):
        squares = ''

        for square in self.board:
            squares += str(square)

        return squares
