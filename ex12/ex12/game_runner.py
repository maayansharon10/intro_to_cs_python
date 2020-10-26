import tkinter as tk
from tkinter import PhotoImage
from .game import *
from .player import *
from .ui import *


class Controller:
    """
    This class is has all utilities in order to run a game.
    It uses class Gui for visual display.
    """

    def __init__(self):
        self.game = Game()
        self._dict_of_players = {3: "h"}
        self.num_of_players = 2
        self.turns_counter = 0
        self.ai_player_flow1 = None
        self.ai_player_flow2 = None

    def play(self):

        self.gui = UI(self)
        self.gui.root.mainloop()

    def reset_game(self):
        self.game = Game()
        self._dict_of_players = {}
        self.turns_counter = 0
        self.ai_player_flow1 = None
        self.ai_player_flow2 = None

    def _end_game_handler(self):
        """find who is the winner, and show end of game screen to user"""
        # check if game is over
        winner = self.game.get_winner()
        self.gui.game_over_screen(winner)

    def count_turn(self):
        """
        Advance the game turns counter in one
        """

        self.turns_counter += 1

    def get_current_player_type(self, name):
        """
        returns the player who has this turn
        :param name: int
        """

        return self._dict_of_players[name][1]

    def add_players(self, player_type_lst):
        """
        Adds players of class HumanPlayer or AiPlayer, according to list of
        types
        :param player_type_lst:
        """

        for i in range(0, self.num_of_players):  # for each new player,
            # add to dictionary of players: {player_name: pointer_to_object,
            #  type}

            player_type = player_type_lst[i]
            AI_Activated = False

            if player_type == "h":
                new_player = HumanPlayer(self.game, i + 1)
                self._dict_of_players[i + 1] = new_player, player_type

            elif player_type == "m":
                new_player = AiPlayer(self.game, i + 1)
                self._dict_of_players[i + 1] = new_player, player_type
                if not AI_Activated:
                    self.first_ai_player()  # Activates ai players

    def is_game_over(self):
        """check if game over
        :return True upon success, False otherwise"""

        """get winner from game, and determine if game is over"""

        if self.game.get_winner() != None:  # get winner from game (0,1 or 2)
            # A winner was found, or it's a tie!
            return True

        return False  # we have got None - Game is still on!

    def _did_ran_out_of_turns(self):
        """if the game ran out of turns - return True, else - False"""

        num_of_cells_in_board = self.game.board.get_num_of_cells_in_board()

        if self.turns_counter > num_of_cells_in_board:
            # number of cells in board is greater than num of turns
            # (greater-not all cells have disks, equal -if it's the last turn)
            return True
        else:
            return False

    def _is_board_full(self):
        """checks if board is full or not.
        :return True upon success"""
        return self.game.board.is_board_full

    ######## Flow of a Move ##########

    def on_col_selected(self, col):
        """Been called when a button is pressed on board of Gui.
        advance game, according to choice:
        - puts a disk on board
        - dsiplay updated board
        - checks if game is over
        returns a function which does all of that and will be used by button"""

        def update_move():
            player = self.game.get_current_player()
            # care about the choice only if it's a human player turn:
            if not self.is_game_over() and \
                    self.get_current_player_type(player) == "h":
                try:
                    self.game.make_move(col)  # put disk in board
                except:
                    self.gui.wrong_move_windows()  # If wrong move has been
                    # chosen, pop a special window and ignore the exception

                self.gui.draw_board()  # display updated screen
                if self.is_game_over():  # check if game is still on
                    self._end_game_handler()

        return update_move

    ######## Next functions run ai players, and call each other ########
    def first_ai_player(self):
        """Manages a flow of a computer-based-player"""

        if not self.is_game_over():
            player = self.game.get_current_player()
            if self.get_current_player_type(player) == "m" and player == 1:

                next_move = self._dict_of_players[player][0].choose_move()
                self.game.make_move(next_move)
                self.gui.draw_board()
                if self.is_game_over():
                    self._end_game_handler()

            self.gui.root.after(800, self.second_ai_player)

    def second_ai_player(self):
        """Manages a flow of a computer-based player"""

        if not self.is_game_over():
            player = self.game.get_current_player()
            if self.get_current_player_type(player) == "m" and player == 2:
                next_move = self._dict_of_players[player][0].choose_move()
                self.game.make_move(next_move)
                self.gui.draw_board()
                if self.is_game_over():
                    self._end_game_handler()

            self.gui.root.after(800, self.first_ai_player)
