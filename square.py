class Square:

    def __init__(self, row, column):

        self.row = row
        self.column = column
        self.is_visible = True
        self.is_marked = False
        self.is_water = False
        self.is_ship = False
        self.is_border = False

    def apply_color(self):
        pass

    def __str__(self):

        if self.is_marked:
            return "X"
        elif self.is_visible:
            return "O"
        return " "
