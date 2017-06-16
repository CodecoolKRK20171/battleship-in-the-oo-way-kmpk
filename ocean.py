from square import Square


class Ocean:
    """Class responsible for drawing and handling the playable area"""

    def __init__(self, owner):
        """Initialize function. Responsible for handling the playable area.

        Args:
            owner: Owner of the ship.

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
        """Set the status of the square objects to make them
            ships.

        Args:
            none

        Returns:
            none

        """

        for ship in self.ships:

            for coords in ship.coordinates:
                self.board[coords[1]][coords[0]].make_ship()

    def check_if_sunk(self, player):
        """Checks if the given ship is sunk.

        Args:
            player: <-- player ships.

        Returns:
            none

        """

        for ship in self.ships:

            for coords in ship.coordinates:
                if not self.board[coords[1]][coords[0]].is_marked:
                    break
            else:
                ship.sunk_a_ship()
                self.make_borders(ship)
                player.check_if_alive(self)

    def make_borders(self, ship):
        """Creates borders around the sunk ship.

        Args:
            ship: The ship which borders are supposed to be drawn around.

        Returns:
            none

        """

        for coords in ship.border:

            try:
                target = self.board[coords[1]][coords[0]]

            except IndexError:
                pass

            else:
                target.make_border()
                target.show()

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
