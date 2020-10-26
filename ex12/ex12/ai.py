from .game import *
from .board import *
import copy



class AI:
    """ this class creates an instance of type AI which function as the
    'brain' of a player in 4 in a row game"""

    def __init__(self, game, player):
        """constractor of the class. create an instance of type AI
        :param game of type Game()
        :param player - name of player (int)"""
        
        self.game = game
        self.player = player  # name of player

    def get_player_name(self):
        """return player name"""
        return self.player

    def find_legal_move(self, timeout=None):
        """func the best legal move in depth of 3. raise exception if game
        is over and there's no legal move left to do.
        :return next_move - int, num of column
         """
        # min max algorithm to find best next move in depth of 3.
    
        if self.game.board.is_board_full():
            raise ("No possible AI moves")
        else:
            board = self.game.board
            player = self.player
            # get the best move in depth of 3:
            next_move = self.get_best_move(board, player)
            return next_move

    def get_board_score(self, board, player):
        """ calculate a board score for player, given his rival's board
        score
        :param board - type Board
        :param player - int represent current player
        :return final score"""
        
        rival = (player + 1) % 2  # calculate rival's number

        return (self.get_board_score_helper(board, player) -
                self.get_board_score_helper(board, rival))
    
    def get_board_score_helper(self, board, player):
        """a helper func for get_score_board.
        gives a current board a score. checks all options for scores for
        1 - 4 in a row, then returns max score
        :param board - type board
        :param player - int
        :return board's score"""
        options_for_scores = []
        # check if there's one disk in a row:
        one_iar = board.is_there_x_in_a_row(player, 1)
        if one_iar > 0:
            one_score = one_iar  # set a score
            options_for_scores.append(one_score)
            
        # check if there're two disks in a row:
        two_iar = board.is_there_x_in_a_row(player, 2)
        if two_iar > 0:
            two_score = two_iar * 10  # set a score
            options_for_scores.append(two_score)
        
        # check if there're three in a row :
        three_iar = board.is_there_x_in_a_row(player, 3)
        if three_iar > 0:
            three_score = three_iar * 100  # set a score
            options_for_scores.append(three_score)
        
        # check if there're four in a row :
        four_iar = board.is_there_x_in_a_row(player, 4)
        if four_iar > 0:
            four_score = four_iar*1000  # set a score
            options_for_scores.append(four_score)
        max_val = max(options_for_scores)
        
        return max_val
        
    def get_best_move(self, board, player):
        """func calc best move in depth of 3 with helper func name
        score_board.
        :param board of type board
        :param player - int
        :return best_move - int represent best col to choose
        """
        depth = 3
        optional_moves = board.get_all_valid_col()  # all valid cols of board
        best_move = -1
        best_score = -1000000000
        
        for col in optional_moves:
            new_board = copy.deepcopy(board)  # copy of object of type
            # Board()
            new_board.add_disk_to_board(col,player)  # add disk at col 'move'
            
            # given that this is player's turn :
            board_score = self.score_board(new_board, player, True, depth-1)
            
            if board_score > best_score:
                best_score = board_score
                best_move = col
        
        return best_move
    
    def score_board(self, board, for_player, is_player_turn, depth):
        """calculate score of board with recursion.
        :param board of type Board
        :param for_player - int represent the current player
        :param is_player_turn - bool
        :param depth - of recursion"""

        # when recursion stops:
        if depth == 0:
            # return the score of a board for player given rival's score
            return self.get_board_score(board, for_player)
        
        # cur_player's turn calc move:
        if is_player_turn:
            # get all valid columns as optional moves
            optional_moves = board.get_all_valid_col()
            
            best_score = -1000000000  # initial best score
            
            for col in optional_moves:
                new_board = copy.deepcopy(board)  # copy of object of type
                # Board()
                new_board.add_disk_to_board(col,for_player)  # add disk at col
                # 'move'

                board_score = self.score_board(new_board, for_player,
                                              not is_player_turn, depth - 1)
                if board_score > best_score:
                    best_score = board_score
            return best_score
        else:
            # Evil's (other player)  turn, calc move
            optional_moves = board.get_all_valid_col()# all valid cols of board
            worst_score = 1000000000  # initial best score
            for col in optional_moves:
                new_board = copy.deepcopy(board)  # copy of object of type
                # Board()
                new_board.add_disk_to_board(col,for_player)  # add disk at col
                # 'move'
                board_score = self.score_board(new_board, for_player,
                                              not is_player_turn, depth - 1)
                if board_score < worst_score:
                    worst_score = board_score
            return worst_score

    def get_last_found_move(self):

        pass
