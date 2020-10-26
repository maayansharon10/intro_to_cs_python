from .board import *
from itertools import cycle


class Game:

    def __init__(self):
        self.board = Board(6, 7)
        self._turns_iterator = cycle(range(1, 3))
        self._current_player = next(self._turns_iterator)

    def make_move(self, column):
        """recognize current player, try to add a disk
        This function might raise an exception:
        - if game is not over
        - if couldn't add disc to board"""

        cur_player_disk = self.get_current_player()
        if self.get_winner() != None:  # Game is not over
            raise IndexError("player one has won. Cannot make another move.")

        self.board.add_disk_to_board(column, cur_player_disk)
        # Might raise an exception

        self._current_player = next(self._turns_iterator)  # advance to next
        # player

    def get_player_at(self, row, col):
        """:return int representing a player which disk is in a
        certain cell. if no disk in cell - returns None.
        :exception if cell out of board - raise: illegal move"""

        try:
            player = self.board.who_in_this_cell(row, col)
            if player == 0:
                return None
            else:
                return player
        except:
            IndexError("Illegal Location")

    def get_current_player(self):
        """ :return num of current player (int)"""

        return self._current_player

    def get_winner(self):
        """Checks the winning status:
        If no victory was achieved, returns None.
        If one of the players won, returns 1 or 2.
        If a tie exists, returns 0"""

        for player in range(1, 3):
            if self.board.is_there_4_in_a_row(player):
                return player
        if self.board.is_board_full():
            return 0
        else:
            return None
