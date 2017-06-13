class Square:
    def __init__(self, row, column):
        self.is_marked = True
        self.row = row
        self.column = column

    def __str__(self):

        if self.is_marked:
            mark = 'x'
        else:
            mark = '0'
        return mark


class Ship:
    def __init__(self, positions):
        self.positions = positions
        self.squares = []
        for i in range(len(self.positions)):
            square = Square(self.positions[i][0], self.positions[i][1])
            self.squares.append(square)

    def __str__(self):
        ship7 = ''
        for i in range(len(self.squares)):
            ship7 += str(self.squares[i])
        return ship7


class Ocean:

    def __init__(self):
        self.ships = []
        self.board = []

    def __str__(self):
        return '\n'.join([''.join(row) for row in self.board])

    def add_ship(self, position_x, position_y, size, is_horizontal=False):
        positions = []

        for i in range(size):
            if is_horizontal:
                position_x += 1
            else:
                position_y += 1
            positions.append((position_x, position_y))

        positions = tuple(positions)
        self.ships.append(Ship(positions))

    def fill_board(self):
        for i in range(0, 10):
            self.board.append([' ']*10)

        for ship in self.ships:
            for square in ship.squares:
                self.board[square.column][square.row] = str(square)


def main():
    ship = Ship(((2, 3), (2, 4), (2, 5)))
    ocean = Ocean()
    ocean.add_ship(2, 3, 4, True)
    ocean.add_ship(7, 3, 2, False)
    ocean.fill_board()
    print(ocean)


if __name__ == "__main__":
    main()
