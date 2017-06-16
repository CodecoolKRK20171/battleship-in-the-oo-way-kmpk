def get_possible_coords():
    """Function creates a list with all possible coordinates in the
        letter-number convention.

    Args:
        none

    Returns:
        possible_chords: List with all the possible coordinates.

    """
    possible_coords = []

    for letter in "abcdefghij":

        for number in range(0, 10):
            possible_coords.append(letter + str(number))

    return possible_coords


def convert_coords(coord):
    """Converts the coordinates from letter-number convention
        to a number-number convention.

    Args:
        coord: Coordinate to convert.

    Returns:
        position_x : X coordinate.
        position_y : Y coordinate.

    """
    position_x = "abcdefghij".index(coord[0].lower())
    position_y = int(coord[1])

    return position_x, position_y


def convert_coords_reverse(coord):
    """Converts the coordinates from number-number convention
        to a letter-number convention.

    Args:
        coord: Coordinate to convert.

    Returns:
        coord: Converted coordinate.

    """

    if coord != "Nothing":
        position_x = "ABCDEFGHIJ"[coord[0]]
        position_y = str(coord[1])
        return position_x + position_y

    else:
        return coord


def add_colors():
    """Creates a dictionary with colors.

    Args:
        none

    Returns:
        colors: Dictionary with colors.

    """
    colors = {"blue": "\033[1;34m",
              "red": "\033[1;31m",
              "yellow": "\033[1;33m",
              "green": "\033[0;32m",
              "reset": "\033[0;0m"}

    return colors
