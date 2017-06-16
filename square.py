import common


class Square:
    """Class responsible for creating and handling square objects"""

    def __init__(self, row, column, is_visible=False):
        """Initialize function. Creates a square object.

        Args:
            row: The row of the square.
            column: Column of the square.
            is_visible: Is the square visible,

        Returns:
            none

        """
        self.row = row
        self.column = column
        self.is_visible = is_visible
        self.is_marked = False
        self.is_water = True
        self.is_ship = False
        self.is_border = False

    def apply_color(self, mark):
        """Applies coloros to the squares.

        Args:
            mark: Is the square marked for coloring.

        Returns:
            sign: Colored square.

        """

        colors = common.add_colors()

        if self.is_water:
            sign = colors["blue"] + mark + colors["reset"]

        if self.is_visible:
            if self.is_border:
                sign = colors["yellow"] + mark + colors["reset"]

            elif self.is_ship:
                sign = colors["green"] + mark + colors["reset"]

            if self.is_marked:
                sign = colors["red"] + mark + colors["reset"]

        return sign

    def mark(self):
        """Set the is_marked attribute to True.

        Args:
            none

        Returns:
            none

        """

        self.is_marked = True
        self.show()

    def make_ship(self):
        """Sets the is_ship attribute to True.

        Args:
            none

        Returns:
            none

        """
        self.is_ship = True

    def show(self):
        """Sets the is_visible attribute to True.

        Args:
            none

        Returns:
            none

        """
        self.is_visible = True

    def hide(self):
        """Sets the is_visible attribute to False.

        Args:
            none

        Returns:
            none

        """
        self.is_visible = False

    def make_border(self):
        """Sets the is_border attribute to True.

        Args:
            none

        Returns:
            none

        """
        self.is_border = True

    def __str__(self):
        """Magic function used for square printing.

        Args:
            none

        Returns:
            colored_mark: Square object converted to a string.

        """
        mark = "╶"  # -
        if self.is_ship:
            mark = "▢"  # Θ
        if self.is_marked:
            mark = "⊠"  # ◼ ✔ X
        if self.is_border:
            mark = "☼"  # x *
        if not self.is_visible:
            mark = "⟡"  # ≈

        colored_mark = self.apply_color(mark)
        return colored_mark
