from square import Square


class Ocean:

    def __init__(self, owner):
        self.ships = []
        self.board = []
        self.owner = owner

    def fill_board(self):
        for i in range(0, 10):
            temp_list = []
            for j in range(0, 10):
                temp_list.append(Square(i, j))
            temp_list.append("\n")
            self.board.append(temp_list)

    def __str__(self):
        squares = ''

        for square in self.board:
            for square2 in square:
                squares += str(square2)

        return squares
