from ai import AI
import common


class Player:

    def __init__(self, name):
        """Initialize function for the Player class.
            Creates the player with name, is_alive, and previous_shot attributes.

        Args:
            name: Player name.

        Returns:
            none.

        """
        self.name = name
        self.is_alive = True
        self.previous_shot = "Nothing"

    def shoot_on_board_player(self, battlefield, coords):
        """Shot made by the player.

        Args:
            battlefield: Playable area.
            coord: X, Y coordinates of the shot player wants to make.

        Returns:
            none

        """
        pos_y, pos_x = common.convert_coords(coords)
        target = battlefield.board[pos_x][pos_y]

        if target.is_ship:
            target.mark()
        else:
            target.show()

    def shoot_on_board_ai(self, board):
        """Shot made by the AI.

        Args:
            board: Playable area.

        Returns:
            target: Coords of the shot made by AI.

        """
        ai = AI()
        target = ai.shoot_on_board_ai(board)
        self.previous_shot = target
        return target

    def check_if_alive(self, board):
        """Checks if the player ships are sunk.

        Args:
            board: Playable area.

        Returns:
            none

        """
        for ship in board.ships:
            if not ship.sunk:
                break
        else:
            self.is_alive = False

    def __str__(self):
        """__str__ magic function. Used for username printing.

        Args:
            none

        Returns:
            Name attribute converted into a string.

        """
        return str(self.name)
