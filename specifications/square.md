## Specification

### Class Square

__Attributes__

* `column`
  - data: int
  - description: a horizontal position of a Square

* `row`
  - data: int
  - description: a vertical position of a Square

* `is_marked`
  - data: bool
  - description: True if square was hit by other player, False otherwise. Default is False

* `is_visible`
  - data: bool
  - description: True if square should be visible on board, False otherwise. Default is False

__Instance methods__

* ##### ` __init__(self, row, column)`

  Constructs a Square object
  Raises TypeError if type of any argument is incorrect

* `mark(self)`

  Sets the object's * is_marked * attribute to True

* `show(self)`

  Sets the object's * is_visible * attribute to True

* `__str__(self)`

  Returns a formatted string of * Square * depending on its attributes.
  "X" for marked, "O" for unmarked, " " for hidden
