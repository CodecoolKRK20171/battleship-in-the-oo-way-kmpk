import common


class Square:

    def __init__(self, row, column, is_visible=False):

        self.row = row
        self.column = column
        self.is_visible = is_visible
        self.is_marked = False
        self.is_water = True
        self.is_ship = False
        self.is_border = False

    def apply_color(self, mark):

        colors = common.add_colors()

        if self.is_water:
            sign = colors["blue"] + mark + colors["reset"]
        if self.is_visible:
            if self.is_border:
                sign = colors["cyan"] + mark + colors["reset"]
            elif self.is_ship:
                sign = colors["green"] + mark + colors["reset"]
            if self.is_marked:
                sign = colors["red"] + mark + colors["reset"]

        return sign

    def mark(self):

        self.is_marked = True
        self.show()

    def make_ship(self):

        self.is_ship = True

    def show(self):

        self.is_visible = True

    def hide(self):

        self.is_visible = False

    def make_border(self):

        self.is_border = True

    def __str__(self):

        mark = "."
        if self.is_ship:
            mark = "S"
        if self.is_marked:
            mark = "X"
        if self.is_border:
            mark = "*"
        if not self.is_visible:
            mark = "-"

        colored_mark = self.apply_color(mark)
        return colored_mark
