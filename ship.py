class Ship:

    ships = {"Carrier": 5,
             "Battleship": 4,
             "Cruiser": 3,
             "Submarine": 3,
             "Destroyer": 2}
    taken_coord_list = []  # lista tupli koordynatow ktore sa zakazane

    def __init__(self, start_position, is_vertical, name):

        self.sunk = False
        self.size = Ship.ships[name]
        self.start_position = start_position  # tuple
        self.is_vertical = is_vertical  # bool
        self.coordinates = Ship.create_ship(self.start_position, self.is_vertical, self.size)  # list of tuple
        surroundings = Ship.add_coord_around_ship(self.coordinates)  # coords of ships surroundings
        self.border = surroundings
        Ship.add_coord_not_repetitive(Ship.taken_coord_list, self.coordinates)
        Ship.add_coord_not_repetitive(Ship.taken_coord_list, self.border)

    def create_ship(start_position, is_vertical, size):
        coordinates = []
        if is_vertical:
            for i in range(size):
                coordinates.append((start_position[0], start_position[1]+i))
        else:
            for i in range(size):
                coordinates.append((start_position[0]+i, start_position[1]))

        if Ship.check_availability(Ship.taken_coord_list, coordinates):
            return coordinates
        else:
            return False

    def check_availability(coords_taken, coord_to_check):
        # params: lists of tuples
        for coord in coord_to_check:
            if coord in coords_taken or \
                    coord[0] not in range(0, 10) or \
                    coord[1] not in range(0, 10):
                return False
        return True

    def add_coord_around_ship(coordinates):
        additional_coord = []
        for coord in coordinates:
            for x in range(-1, 2):
                for y in range(-1, 2, 1):
                    coord_to_add = (coord[0]+x, coord[1]+y)
                    if coord_to_add not in additional_coord and \
                            coord_to_add not in coordinates and \
                            coord[0] in range(0, 10) and \
                            coord[1] in range(0, 10):
                        additional_coord.append(coord_to_add)
        return additional_coord

    def sunk_a_ship(self):

        self.sunk = True

    def add_coord_not_repetitive(taken_coord_list, coords_to_add):
        for coord in coords_to_add:
            if coord not in taken_coord_list:
                taken_coord_list.append(coord)

    @classmethod
    def set_lists_to_default(cls):
        cls.ships = {"Carrier": 5,
                     "Battleship": 4,
                     "Cruiser": 3,
                     "Submarine": 3,
                     "Destroyer": 2}
        cls.taken_coord_list = []
