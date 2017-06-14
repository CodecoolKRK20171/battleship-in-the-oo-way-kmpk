from square import Square
from copy import deepcopy


class Ocean:

    def __init__(self, owner):
        """Initialize function. Responsible for handling the playable area.

        Args:
            position: Position of a newly made ship.

        Returns:
            none

        """
        self.ships = []
        self.board = []
        self.owner = owner

    def fill_board(self):
        """Fills the board with Square objects.

        Args:
            none

        Returns:
            none

        """
        self.board = []
        for i in range(0, 10):
            temp_list = []
            for j in range(0, 10):
                visibility = True
                if self.owner.name == "AI":
                    visibility = False
                temp_list.append(Square(i, j, visibility))
            self.board.append(temp_list)

    def fill_ship(self):
        for ship in self.ships:
            for coords in ship.coordinates:
                self.board[coords[1]][coords[0]].make_ship()

    # def hide_enemy(self):
    #     for ship in self.ships:
    #         for square in ship.coordinates:
    #             self.board[square[1]][square[0]].hide()

    def __str__(self):
        """Prints out the ocean object.

        Args:
            self: Object carrying attribute:

        Returns:
            ocean: The playable area.

        """
        board_lenght = 10
        ocean = '╔═══╦' + '══' * board_lenght + '═╗\n'
        ocean += '║ \ ║ A B C D E F G H I J ║\n'
        ocean += '╠═══╬' + '══' * board_lenght + '═╣\n'

        for row in self.board:
            ocean += "║ {} ║ ".format(self.board.index(row))
            for square in row:
                ocean += str(square) + " "
            ocean += '║\n'
        ocean += '╚═══╩' + '══' * board_lenght + '═╝\n'

        return ocean
