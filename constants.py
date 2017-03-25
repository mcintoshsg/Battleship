
class Constants:

    # Game Battleships information
    SHIP_INFO = [
        ("Aircraft Carrier", 5),
        ("Submarine", 3),
        ]

    # Ascii constants to add color to text
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    BLACK='\033[30m'
    RED='\033[31m'
    GREEN='\033[32m'
    ORANGE='\033[33m'
    BLUE='\033[34m'
    PURPLE='\033[35m'
    CYAN='\033[36m'
    LIGHTGREY='\033[37m'
    DARKGREY='\033[90m'
    LIGHTRED='\033[91m'
    LIGHTGREEN='\033[92m'
    YELLOW='\033[93m'
    LIGHTBLUE='\033[94m'
    PINK='\033[95m'
    LIGHTCYAN='\033[96m'

    # Primary and Tracker Game Board Sizes
    BOARD_SIZE = 10

    # Constants for ship placement and for hit, miss and sunk
    VERTICAL_SHIP = BOLD + BLUE + '#' + ENDC
    HORIZONTAL_SHIP = BOLD + GREEN + '#' + ENDC
    EMPTY = 'O'
    MISS = BOLD + YELLOW + '@' + ENDC
    HIT = BOLD + RED + '*' + ENDC
    SUNK = '$'

    # Game start display
    BANNER = HEADER + """


              ########     ###    ######## ######## ##       ########  ######  ##     ## #### ########
              ##     ##   ## ##      ##       ##    ##       ##       ##    ## ##     ##  ##  ##     ##
              ##     ##  ##   ##     ##       ##    ##       ##       ##       ##     ##  ##  ##     ##
              ########  ##     ##    ##       ##    ##       ######    ######  #########  ##  ########
              ##     ## #########    ##       ##    ##       ##             ## ##     ##  ##  ##
              ##     ## ##     ##    ##       ##    ##       ##       ##    ## ##     ##  ##  ##
              ########  ##     ##    ##       ##    ######## ########  ######  ##     ## #### ##




      """ + ENDC

     # Game instructions
    INSTRUCTIONS = GREEN + """\n\n\n **********   Battleship Instructions ********

        To win the game you must sink all of your opponents battleships!
        Each player will firstly place 5 battleships on the game board, you do this by
        choosing coordiantes to place the ship and the orientation:
        Cruiser, a,2, vertical. After the placement of each battleship players will
        take turns in trying to to sink a battleship until there is a winner

        Good Luck!!!! \n\n

    """ + ENDC

'''
    SHIP_INFO = [
        ("Aircraft Carrier", 5),
        ("Battleship", 4),
        ("Submarine", 3),
        ("Cruiser", 3),
        ("Patrol Boat", 2)
    ]
'''
