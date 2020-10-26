from board import Board
from car import Car
from helper import load_json
import sys



VALID_CAR_NAME = {'Y', 'B', 'O', 'W', 'G', 'R'}
VALID_CAR_LEN = {2, 3, 4}
VALID_ORIENTATION = {0, 1}


class Game:
    """
    Class of type Game intending to create an run a rush hour game
    """
    MSG = {
        'welcome': 'welcome to the game! ',
        'error_input_msg': 'input not valid, please insert input again',
        'move_msg': 'please inset name,direction for car you wish to move. \n'
                    'note name must be (Y,B,O,W,G,R),\n '
                    'and direction must be one of the following : u,d,l,r\n ',
        'victory' : 'You made it! Good job!'}
        
    def __init__(self, board):
        """ a constractor.
        Initialize a new Game object.
        :param board: An object of type board
        """
        self.board_game = board  # a list list representing board

    def __is_move_input_valid(self, move_input):
        """checks if user input, which is a string for move is valid
        :return True if move_input is valid"""
        direction_set = {'u', 'd', 'l', 'r'}
        car_name_set = {'Y', 'B', 'O', 'W', 'G', 'R'}
        
        # check if input match the pattern "_,_" -
        if len(move_input) == 3 or move_input[1] == ",":
            
            # check if car name is valid and movekey is valid -
            if move_input[0] in car_name_set \
                    and move_input[2] in direction_set:
                
                # input is valid
                return True
        else:
            # input is not valid
            return False
        
    def __single_turn(self):
        """
        The function runs one round of the game :
            1. Get user's input of: what color car to move, and what
                direction to move it.
            2. Check if the input is valid.
            3. Try moving car according to user's input.
        """

        continue_turn = True
        
        while continue_turn:
            print(Game.MSG['move_msg'])
            requested_move = input("please insert your move") #????
            if self.__is_move_input_valid(requested_move):
                # if input is valid - assign name, movekey
                name = requested_move[0]
                movekey = requested_move[2]
                
                # move car :
                if self.board_game.move_car(name, movekey):
                    # if car moved - turn is over
                    continue_turn = False   # to exit loop

    def game_still_going(self):
        """func checks of game is still going. returns True is it does,
        False otherwise"""
        if self.board_game.cell_content(self.board_game.TARGET_CELL) != 'E':
            # no car reached exit
            return True
        else:  # some car reached exit
            return False

    def play(self):
        """
        The main driver of the Game. Manages the game until completion.
        :return: None
        """
        
        # flad if game is over:
        game_is_not_over = self.game_still_going()
        # on first round, no car is at TARGET_CELL, so returns True
        
        print(Game.MSG['welcome'])  # prints welcome msg
        
        print(self.board_game)  # prints current board
        
        while game_is_not_over:
            self.__single_turn()
            game_is_not_over = self.game_still_going()
            print(self.board_game)
        
        print(Game.MSG['victory'])


if __name__ == "__main__":
    if len(sys.argv) == 2:
        FILE_NAME = sys.argv[1]
        
        board_game = Board()
        car_config_dict = load_json(FILE_NAME)  # dict
        
        for car_name in car_config_dict:
            # key of dict is car_name
            if car_name in VALID_CAR_NAME:
                # if car name is valid - get it's data
                # len of car
                length = car_config_dict[car_name][0]
                # location - is a list
                location_raw = car_config_dict[car_name][1]
                # converting location to tuple
                row = location_raw[0]
                col = location_raw[1]
                location = (row, col)  # location as tuple
                orientation = car_config_dict[car_name][2]
                
                if (length in VALID_CAR_LEN) and (
                        location in board_game.cell_list()) and orientation in VALID_ORIENTATION:
                    # if car is in valid len
                    # and if location is in board
                    # and orientation is valid
                    board_game.add_car(
                        Car(car_name, length, location, orientation))
        game1 = Game(board_game)
        game1.play()
