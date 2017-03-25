###### Battleship Board Class ######

from constants import Constants

class Board:

    def __init__(self, board_type):

        self.board_type = board_type

    def build_blank_board(self):
        self.board = []
        for i in range(Constants.BOARD_SIZE):
            board_row = []
            for j in range(Constants.BOARD_SIZE):
                board_row.append(Constants.EMPTY)
            self.board.append(board_row)

        return self.board
