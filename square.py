class Square:

    def __init__(self, row, column):

        self.row = row
        self.column = column
        self.is_visible = True
        self.is_marked = False
        self.is_water = True
        self.is_ship = False
        self.is_border = False

    def apply_color(self, mark):

        colors = {"blue": "\033[1;34m",
                  "red": "\033[1;31m",
                  "yellow": "\033[1;33m",
                  "green": "\033[0;32m",
                  "reset": "\033[0;0m"}

        if self.is_water:
            sign = colors["blue"] + mark + colors["reset"]
        if self.is_border:
            sign = colors["cyan"] + mark + colors["reset"]
        if self.is_ship:
            sign = colors["green"] + mark + colors["reset"]

        return sign

    def mark(self):

        self.is_marked = True

    def make_ship(self):

        self.is_ship = True

    def show(self):

        self.is_visible = True

    def make_border(self):

        self.is_border = True

    def __str__(self):

        mark = "-"
        if self.is_marked:
            mark = "X"
        elif self.is_visible:
            mark = "O"

        colored_mark = apply_color(mark)
        return colored_mark
