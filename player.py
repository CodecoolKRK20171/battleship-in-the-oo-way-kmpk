# from ocean import Ocean
# from ship import Ship


class Player:

    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def shoot_on_board(self, board, x, y):
        if board.board[y][x].is_ship:
            board.board[y][x].mark()
        else:
            board.board[y][x].show()

    def is_alive(self, board):
        available_square_ship = 0
        for row in board:
            for column in row:
                if board.board[row][column].is_ship:
                    available_square_ship += 1
        if available_square_ship == 0:
            return False
        else:
            return True
