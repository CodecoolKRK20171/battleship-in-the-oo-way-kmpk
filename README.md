# Battleship in the OOP way

## The story

## Specification


__main.py__

###BATTLESHIPS


__square.py__

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



__ship.py__

### Class Square

__Attributes__

* `size`
    - data: int
    - description: lenght of ship

* ` is_horizontal`
    - data: boolean
    - description: determinates direction of ship

* `sunk=False`
    - data: boolean
    - description: determinates status of ship, alive or dead

* `start_position`
    - data: tuple
    - description: coordinates of start of ship

* `coordinates`
    - data: list of tuples
    - description: taken coordinates by ship

__class Attributes__

* `ships`
    - data: dict
    - description: key: str(name of ship); value: int(lenght of ship)

* `taken_coord_list`
    - data: list
    - description: list of coordinates that are taken by ships and theirs surroundings

__Instance methods__


* ##### ` __init__(self, start_position, is_horizontal, name)`


    Constructs a Ship object


__ocean.py__

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
