## Specification

### Class Ocean

__Attributes__

* `ships`

  - data: list
  - description: Ship class object.

* `board`

  - data: list
  - description: List of lists, containing playable area.


__Instance methods__

* `__init__(self, positions)`

  Constructs an ocean object. Raises and IndexError if the position is
  out of range of the board attribute.

* `add_ship(self, x, y, size, horizontal=False)`

  Adds a ship of given size, on a given position.
  Parameter horizontal is responsible for creating a ship
  in a horizontal position, and is set to False by default.

* `fill_board(self)`

  Fills the board attribute with playable area and objects.
