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

* `is_water`
    - data: bool
    - description: True if square should be visible on board, False otherwise. Default is False

* `is_ship`
  - data: bool
  - description: True if square should be visible on board, False otherwise. Default is False


* `is_boarder`
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

* `apply_color(self,mark)`

    Return colored square

* `make_ship(self)`

    Sets is_visible atribute to True

* `hide(self)`

    Sets is_visible atribute to False

* `make_boarder(self)`
    Sets is_boarder atribute to True



__ship.py__

### Class Square

__Attributes__

* `size`
    - data: int
    - description: lenght of ship

* ` is_vertical`
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


* `border`
    - data: list of tuples
    - description: list tuples around the ship


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

* `create_ship(start_position, is_vertical, size)`

    create ships coordinates

* `check_availability(coords_taken, coord_to_check)`
    checks if the ship can be placed in the given coordinates


* `add_coord_around_ship(coordinates)`

    adds unshootable coordinates around the sunk ship

* `sunk_a_ship(self)`

    sets sunk atribute to True

* `add_coord_not_repetitive(taken_coord_list, coords_to_add)`

    create a list of already taken coordinates

* `set_lists_to_default(cls)`

    create a list of the possible ships

__ocean.py__

### Class Ocean

__Attributes__

* `ships`

  - data: list
  - description: Ship class object.

* `board`

  - data: list
  - description: List of lists, containing playable area.

* `owner`
    - data: String
    - String with the name of the owner

__Instance methods__

* `__init__(self, positions)`

  Constructs an ocean object. Raises and IndexError if the position is
  out of range of the board attribute.


* `fill_board(self)`

  Fills the board attribute with playable area and objects.

* `fill_ship(self)`

    changes square objects to ships

* `check_if_sunk(self,player)`

    checks if the given ship is sunk

* `make_boarder(self, ship)`
    create border around the sunk ships

* `__str__(self)`

    prints out the ocean objects

__player.py__
###Class player

__attributes__

* `name`
- data:string
- description:Player name

* `is_alive`
- data:bool
- description:True or False


* `previous_shot`
- data:string
- description:


__Instance methods__

* ##### ` __init__(self)`
    user_ship_list = []

    Constructs an list with objects ships


* `shoot_on_board_player(self, battlefield, coords)`

    player shooting method

* `shoot_on_board_player(self, board)`

    AI shooting method

* `check_if_alive(self, board)`

    Checks if the player ships are sunk

* `__str__(self)`
    print user name


* `is_a_life`

    checking users life
