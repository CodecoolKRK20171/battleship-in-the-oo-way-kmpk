def get_possible_coords():

    possible_coords = []
    for letter in "abcdefghij":
        for number in range(0, 10):
            possible_coords.append(letter + str(number))
    return possible_coords


def convert_coords(coord):

    position_x = "abcdefghij".index(coord[0])
    position_y = int(coord[1])

    return position_x, position_y


def convert_coords_reverse(coord):

    if coord != "Nothing":
        position_x = "ABCDEFGHIJ"[coord[0]]
        position_y = str(coord[1])
        return position_x + position_y
    else:
        return coord


def add_colors():

    colors = {"blue": "\033[1;34m",
              "red": "\033[1;31m",
              "yellow": "\033[1;33m",
              "green": "\033[0;32m",
              "reset": "\033[0;0m"}
    return colors
