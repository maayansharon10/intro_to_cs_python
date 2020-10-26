from .ai import *

class Player:
    INSERT_MOVE = "Please insert the column you would like to place your " \
                  "next disk at."
    INVALID_MOVE = "your move is not valid, please try again"
    
    def __init__(self, game, name):
        """constractor of instant of type Player.
        :param color - represent color of his disks.
        :param type can be h - human or m - machine."""

        self.player_name = name
        self.game = game

        # list of tuples (row, col) of all disks player has on board
        self.list_of_disks = []

    def get_player_name(self):
        return self.player_name


class HumanPlayer(Player):

    def __init__(self, game, name):
        Player.__init__(self, game, name)
        self.player_type = "h"
    
    def get_player_type(self):
        return self.player_type
    
    def choose_move(self):
        """player decides on his next move.
        :return move (int represent num of column)"""

        next_move = input(self.INSERT_MOVE)
        next_move = int(next_move)
        return next_move


class AiPlayer(Player):
    
    def __init__(self, game, name):
        Player.__init__(self, game, name)
        self.player_type = "m"
        # create player's brain
        self.brain = AI(self.game, self.player_name)

    def get_player_type(self):
        return self.player_type
    
    def choose_move(self):
        """player decides on his next move.
        :return move (int represent num of column)"""
        next_move = self.brain.find_legal_move()
        return next_move