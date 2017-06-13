## Specification

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

``
