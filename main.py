from ocean import Ocean
from player import Player
from ship import Ship
from ai import AI
from os import system
import csv
import common
import random


def read_ascii(file_name):

    with open(file_name, 'r') as f:
        r = csv.reader(f)
        for row in r:
            print("".join(row))


def create_game():

    system("clear")
    read_ascii('ship.csv')
    determine_number_of_players()
    player_name = ask_for_name()
    ask_for_difficulty()
    player_1st = Player(player_name)
    player_2nd = Player("AI")
    battlefield_1st = Ocean(player_1st)
    battlefield_2nd = Ocean(player_2nd)
    system("clear")
    battlefield_1st.fill_board()
    set_up_board(battlefield_1st, player_1st)
    battlefield_2nd.fill_board()
    set_up_board(battlefield_2nd, player_2nd)

    return battlefield_1st, battlefield_2nd, player_1st, player_2nd


def set_up_board(battlefield, player):

    if player.name == "AI" or player.name == "Cheat":
        Ship.set_lists_to_default()
        ships_list = Ship.ships
        while ships_list:
            add_ships_ai(battlefield, ships_list)
            battlefield.fill_ship()
    else:
        Ship.set_lists_to_default()
        ships_list = Ship.ships
        while ships_list:
            add_ships_player(battlefield, ships_list)
            battlefield.fill_ship()


def determine_number_of_players():

    print("\nMornin' cap'n! How many players will battle? ")
    while True:
        game_mode = input("\n'1' for singleplayer, '2' for multiplayer\n")
        if game_mode == "1":
            break
        else:
            print("\n Dammit! Unsupported game mode :(\n")
    return game_mode


def ask_for_difficulty():

    while True:
        difficulty = input("\nHaaarr. What difficulty ye wants? (easy, medium, hard, nightmare): ")
        if difficulty in ["easy", "medium", "hard", "nightmare"]:
            AI.set_difficulty(difficulty)
            break
        else:
            print("\n Dammit! Unsupported game mode :(\n")


def choose_positions():

    while True:
        choice = input("\nPick a starting point (eg. a1) ")
        if choice.lower() in common.get_possible_coords():
            break
        else:
            print("\nYo! That's nah a proper input dude...\n")
    return choice.lower()


def chose_direction():

    choice = input('\nDo you want the ship to be placed vertical? (y/n): ')
    while choice not in 'yn':
        choice = input('Please enter the right option: ')

    return True if choice == 'y' else False


def choose_name():

    possible_names = [key for key in Ship.ships.keys()]
    colors = common.add_colors()
    formatted_names = colors["red"] + "'" + "', '".join(possible_names) + "'" + colors["reset"]

    name = input('Choose the ship kind, out of: {} '.format(formatted_names))
    while name.title() not in Ship.ships.keys():
        name = input('Enter the right ship name: ')

    return name.title()


def add_ships_player(board, ships_list):

    print(board)

    name = choose_name()
    starting_point = choose_positions()
    start_position = common.convert_coords(starting_point)
    direction = chose_direction()

    if Ship.create_ship(start_position, direction, Ship.ships[name]):
        new_ship = Ship(start_position, direction, name)
        board.ships.append(new_ship)
        system("clear")
        print("\nAye aye! {} succesfully placed!\n".format(name))
        del ships_list[name]
    else:
        print("\nSire, ye can nah put it thar...\n")


def add_ships_ai(board, ships_list):

    possible_names = [key for key in Ship.ships.keys()]
    name = random.choice(possible_names)

    starting_point = random.choice(common.get_possible_coords())
    start_position = common.convert_coords(starting_point)

    direction = random.choice([True, False])

    if Ship.create_ship(start_position, direction, Ship.ships[name]):
        new_ship = Ship(start_position, direction, name)
        board.ships.append(new_ship)
        del ships_list[name]


def ask_for_name():

    while True:
        name = input("\nAhoy! Wha' be yer name?\n")
        if name != "AI":
            return name


def check_end_game(player_1st, player_2nd):
    if not player_1st.is_alive:
        read_ascii('lose_screen.csv')
        exit()
    if not player_2nd.is_alive:
        read_ascii('win_screen.csv')
        exit()


def print_boards(battlefield_1st, battlefield_2nd):

    colors = common.add_colors()
    previous_shot_target = common.convert_coords_reverse(battlefield_2nd.owner.previous_shot)

    print(colors["yellow"] + "  * * * YOUR BOARD * * *  \n" + colors["reset"])
    print(battlefield_1st)
    print(colors["yellow"] + " * * * ENEMY BOARD * * *  \n" + colors["reset"])
    print(battlefield_2nd)
    print("\nAhoy. Last turn yer squrvy enemy shot at {}\n".format(previous_shot_target))


def ask_for_positions():

    while True:
        target = input("Where do ye wants t' shoot? (eg. a1)\n")
        if target.lower() in common.get_possible_coords():
            break
        else:
            print("\nYo! Enter correct coords mate...\n")
    return target


def handle_shooting_phase(battlefield_1st, battlefield_2nd, player_1st, player_2nd):
    target = ask_for_positions()
    player_1st.shoot_on_board_player(battlefield_2nd, target)
    battlefield_2nd.check_if_sunk(player_2nd)
    ai_target = player_2nd.shoot_on_board_ai(battlefield_1st)
    battlefield_1st.check_if_sunk(player_1st)


def main():

    battlefield_1st, battlefield_2nd, player_1st, player_2nd = create_game()
    while True:
        system("clear")
        print_boards(battlefield_1st, battlefield_2nd)
        handle_shooting_phase(battlefield_1st, battlefield_2nd, player_1st, player_2nd)
        check_end_game(player_1st, player_2nd)


if __name__ == "__main__":
    main()
