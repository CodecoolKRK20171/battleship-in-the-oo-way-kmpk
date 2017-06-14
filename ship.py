
class Ship:

    ships = {"Carrier": 5, "Battleship": 4, "Cruiser": 3, "Submarine": 3, "Destroyer": 2}
    taken_coord_list = []  # lista tupli koordynatow ktore sa zakazane

    def __init__(self, start_position, is_horizontal, name):

        self.size = Ship.ships[name]
        self.start_position = start_position  # tuple
        self.is_horizontal = is_horizontal  # bool
        self.coordinates = Ship.create_ship(self.start_position, self.is_horizontal, self.size)  # list of tuple
        self.sunk = False
        Ship.taken_coord_list += self.coordinates  # adds coordinates of created ship to Ship.taken_coord_list
        surroundings = Ship.add_coord_around_ship(self.coordinates)  # coords of ships surroundings
        Ship.add_coord_not_repetitive(Ship.taken_coord_list, surroundings)

    def create_ship(start_position, is_horizontal, size):
        coordinates = []
        if is_horizontal:
            for i in range(size):
                coordinates.append((start_position[0], start_position[1]+i))
        else:
            for i in range(size):
                coordinates.append((start_position[0]+i, start_position[1]))

        if Ship.check_availability(Ship.taken_coord_list, coordinates):
            return coordinates
        else:
            return False
            return Ship.taken_coord_list[0]

    def check_availability(coords_taken, coord_to_check):
        # params: lists of tuples
        for coord in coord_to_check:
            # print(coord)
            if coord not in coords_taken and \
                    0 <= coord[0] < 10 and \
                    0 <= coord[1] < 10:
                result = True
            else:
                result = False

        return result

    def add_coord_around_ship(coordinates):
        additional_coord = []
        for coord in coordinates:
            for x in range(-1, 2):
                for y in range(-1, 2, 1):
                    coord_to_add = (coord[0]+x, coord[1]+y)
                    if coord_to_add not in additional_coord:
                        additional_coord.append(coord_to_add)
        return additional_coord

    def add_coord_not_repetitive(taken_coord_list, coords_to_add):
        for coord in coords_to_add:
            if coord not in taken_coord_list:
                taken_coord_list.append(coord)

    @classmethod
    def clear_list(cls):
        cls.taken_coord_list = []
