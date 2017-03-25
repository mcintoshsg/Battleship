# BASIC BATTLESHIP GAME
# Stuart McIntosh
# 24/03/2017
# Version 1.0

import os
import sys


from board import Board
from constants import Constants
from player import Player
from utils import clear_screen, display_instructions, display_welcome_screen

# There are 2 playesr per game the followimng function creates 2 players from the
# Player class and calls the method to get their names whch will be used
# throughout the duration of the game
def get_players():

    players = []

    player1 = Player()
    player2 = Player()

    players.append(player1.get_name(1))
    players.append(player2.get_name(2))

    return players

# The following function displays the different types of game board per player
# A blank board is used in the game setup to place the battleships
# A primary game board is used to identify where ships are located and either hit or missed
# A tracker baord is used to track the attacks players have made on components boards
def display_board(player, board_type, board):

    clear_screen()

    print("\n\n***** {} {} BATTLESHIP GAME BOARD *****\n".format(player.upper(), board_type))
    print("   " + "  ".join([chr(c) for c in range(ord('A'), ord('A') + Constants.BOARD_SIZE)]))

    row_num = 1
    for row in board:
        print(str(row_num).rjust(2) + " " + ("  ".join(row)))
        row_num += 1

    print("\n")

# The following function is part of the game setup and iterates through all the
# ships and places them on the players primary board
def place_battleships(players, blank_board, board):

    player1_boards = []
    player2_boards = []
    player1_ship_locs = []
    player2_ship_locs = []

    clear_screen()

    for player_pos, player in enumerate(players):
        display_board(player, 'BLANK', blank_board)
        for ship in Constants.SHIP_INFO:
            try_again = True
            while try_again:
                start_coords = get_coordinates(ship, player, message='setup_game')
                v_o_h = get_v_o_h(player)
                error = check_placement(blank_board, ship[1], start_coords, v_o_h)
                if error == True:
                    print("You cannot place the {} in that location".format(ship[0]))
                else:
                    pb, pb1_shiplocs, pb2_shiplocs = build_board(blank_board, player1_ship_locs, player2_ship_locs, player_pos, ship[0], ship[1], start_coords, v_o_h)
                    display_board(player, 'PRIMARY', pb)
                    try_again = False
        if player_pos == 0:
            player1_boards.append(pb)
        else:
            player2_boards.append(pb)

        input("{} your game board setup is completed! Hit Enter to continue : ".format(player))
        blank_board = board.build_blank_board()

    return player1_boards, player2_boards, pb1_shiplocs, pb2_shiplocs

# The following function is part of the game setup to get the ship
# coordinates (location on the primary) from the player
def get_coordinates(ship, player, message):

    if message == 'setup_game':
        msg = '{} enter the start coordinates for the {} i.e. a,2 : '.format(player, ship[0])
    else:
        msg = '\n\n{} enter the attack coordinates i.e. a,2 : '.format(player)

    while True:
        user_input = input(msg)
        try:
            coordinates = user_input.split(",")
            if len(coordinates) < 2:
                raise Exception("Invalid entry, too few/many coordinates.")

            if coordinates[0].upper() not in 'ABCDEFGHIJ':
                raise Exception("Invalid entry, you enter value between A and J")

            if str(coordinates[1]) not in '1 2 3 4 5 6 7 8 9 10':
                raise Exception("Invalid entry, you must enter a value between 1 and 10")
            else:
                return coordinates

        except ValueError:
            print ("Invalid entry. Please enter only numeric values for coordinates")
        except Exception as error:
            print(error)

# The following function is part of the game setup to get the ship
# orientation, either vertical or horizontal from the player
def get_v_o_h(player):

    while True:
        v_o_h = input("{} enter the ship's orientation either v for vertical or h for horizontal : ".format(player))
        if v_o_h == "v" or v_o_h == "h":
            return v_o_h
        else:
            print ("Invalid input. Please enter v or h")

# The following function is part of the game setup to ensure that the
# location the player wants to place the ship is within the parmaters of the
# board and also that it does not overlap with another already placed ship
def check_placement(board, ship, start_coords, v_o_h):

    error = False

    y, x = start_coords
    y = ord(y) - 97
    x = int(x)

    if v_o_h == 'v' and x+ship > 10:
        error = True
    elif v_o_h == 'h' and y+ship > 10:
        error = True
    else:
        if v_o_h == 'v':
            for i in range(ship):
                if board[(x+i) - 1][y] != Constants.EMPTY:
                    error = True
        elif v_o_h == 'h':
            for i in range(ship):
                if board[x - 1][y+i] != Constants.EMPTY:
                    error = True
    return error

# The following function takes all the input from the player and stores into a
# list depicting the baord layout ready to be displayed
def build_board(board, player1_ship_locs, player2_ship_locs, player_pos, ship, ship_size, start_coords, v_o_h):

    y,x = start_coords
    tmp = ''

    y = ord(y) - 97
    x = int(x)

    if v_o_h == 'v':
        for a in range(ship_size):
            board[((x + a) - 1)][y] = Constants.VERTICAL_SHIP
            sc = ((x + a) - 1, y)
            tmp = tmp + str(sc)

    elif v_o_h == 'h':
        for b in range(ship_size):
            board[x - 1][y+b] = Constants.HORIZONTAL_SHIP
            sc = (x - 1, y + b)
            tmp = tmp + str(sc)

    if player_pos == 0:
        player1_ship_locs.append(ship)
        player1_ship_locs.append(str(ship_size))
        player1_ship_locs.append(tmp)
    else:
        player2_ship_locs.append(ship)
        player2_ship_locs.append(str(ship_size))
        player2_ship_locs.append(tmp)

    return board, player1_ship_locs, player2_ship_locs

# The following function is part of the actual game where each player attacks their
# oppenents board and check to see if they hit or missed with theior attack
def check_hit_or_miss(start_coords, player, attack_board, tracking_board, ship_locs):

    y, x = start_coords
    y = ord(y) - 97
    x = int(x) - 1
    play_again = False

    attack_coords = x, y

    if attack_board[x][y] == Constants.VERTICAL_SHIP or attack_board[x][y] == Constants.HORIZONTAL_SHIP:
        attack_board[x][y] = Constants.HIT
        tracking_board[x][y] = Constants.HIT
        check_sunk = ship_hits(player, ship_locs, attack_coords)
        play_again = True
    elif attack_board[x][y] == Constants.EMPTY:
        attack_board[x][y] = Constants.MISS
        tracking_board[x][y] = Constants.MISS
        play_again = False
        input("{} you missed!!".format(player))
    else:
        input("{} you have already attacked that position :) ".format(player))
        play_again = True

    return attack_board, tracking_board, play_again

# The following function is part of the actual game if the player hits a ship
# this function will do 2 things - 1: check if the ship has been sunk.
# 2: check to see if all ships have been sunk
def ship_hits(player, ship_locs, attack_coords):

    ship = ''
    hit_points = ''

    for i in ship_locs:
        if str(attack_coords) in i:
            ship = ship_locs[(ship_locs.index(i) - 2)]
            hit_points = ship_locs[(ship_locs.index(i) - 1)]
            hit_points = int(hit_points) - 1
            if int(hit_points) == 0:
                input("{} you have SUNK the {} ".format(player, ship))
                ship_locs[(ship_locs.index(i) - 1)] = str(hit_points)
                if check_winner(ship_locs) == True:
                    clear_screen()
                    input("{} you are the winner!!!".format(player))
                    play_another_game()
            else:
                input("{} you hit one of the battleships!!".format(player))
                ship_locs[(ship_locs.index(i) - 1)] = str(hit_points)


# The following function is part of the actual game if the player hits a ship
# this function check to see if all the ships are sunk and decalre a winner
def check_winner(ship_locs):

    ctr = 0
    for i in ship_locs:
        if i == '0':
            ctr += 1
            if ctr == len(Constants.SHIP_INFO):
                return True
    return False

# The game has been won and the following function asks if the players want to
# play another game
def play_another_game():

    clear_screen()

    while True:
        play_again = input("Do you want to play another game Y/n :")
        if play_again.upper() == 'Y':
            setup_game()
        elif play_again.upper() == 'N':
            sys.exit()
        else:
            print("You must enter - Y/n")

# The following function is the main game loopp where each player takes a turn
# to attck each others primary board
def start_game_loop(pb1, pb2, pb1_shiplocs, pb2_shiplocs, players):

    keep_going = True
    play_again = True
    ship = ''
    message = ''

    clear_screen()

    tracking_board_player1 = Board('TRACKER')
    tracking_board_player2 = Board('TRACKER')
    pb1.append(tracking_board_player1.build_blank_board())
    pb2.append(tracking_board_player2.build_blank_board())

    while keep_going == True:
        for player_pos, player in enumerate(players):
            play_again = True
            while play_again == True:
                start_coords = get_coordinates(ship, player, message)
                if player_pos == 0:
                    h_o_m = check_hit_or_miss(start_coords, player, pb2[0], pb1[1], pb2_shiplocs)
                    pb2[0], pb1[1], play_again = h_o_m
                    display_board(player, 'PRIMARY', pb1[0])
                    display_board(player, 'TRACKER', pb1[1])
                else:
                    h_o_m = check_hit_or_miss(start_coords, player, pb1[0], pb2[1], pb1_shiplocs)
                    pb1[0], pb2[1], play_again = h_o_m
                    display_board(player, 'PRIMARY', pb2[0])
                    display_board(player, 'TRACKER', pb2[1])

# The following function sets the game up ready to play
def setup_game():

    board = Board('BLANK')

    blank_board = board.build_blank_board()

    clear_screen()

    display_welcome_screen()

    players = get_players()

    pb1, pb2, pb1_shiplocs, pb2_shiplocs = place_battleships(players, blank_board, board)

    start_game_loop(pb1, pb2, pb1_shiplocs, pb2_shiplocs, players)

if __name__ == '__main__':

    setup_game()
