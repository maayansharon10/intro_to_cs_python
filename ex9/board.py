

class Board:
    """
    constacts an object of type board with cars on it,
    operates methods on board according to board limitation,
    for example moves cars around
    according to board's limits.
    """
    BOARD_SIZE = 7
    VAILD_LOCATION = [0, 1, 2, 3, 4, 5, 6]
    TARGET_CELL = (3, 7)
    TARGET_CELL_START_VALUE = 'E'
    EMPTY_CELL = "_"
    VERTICAL = 0
    HORIZONTAL = 1
    
    def __init__(self):
        """A constructor for a Board object"""
        # implement your code and erase the "pass
        # Note that this function is required in your Board implementation.
        # However, is not part of the API for general board types.
        board = []
        self.__board_height = Board.BOARD_SIZE
        self.__board_width = Board.BOARD_SIZE
        for row in range(self.__board_height):
            row_lst = []
            for col in range(self.__board_width):
                row_lst.append(Board.EMPTY_CELL)
                
            if row == 3:
                row_lst.append('E')
            board.append(row_lst)
            
        self.board = board

        self.__car_dict = dict()  # cars on board . board starts with no cars
        # {car_name: object from type Car}
        
    def __str__(self):
        """
        This function is called when a board object is to be printed.
        :return: A string of the current status of the board
        """
        # The game may assume this function returns a reasonable representation
        # of the board for printing, but may not assume details about it.
        string_to_print = ""
        for row in range(self.__board_height):
            for col in range(self.__board_width):
                if col == (self.__board_width - 1) and row == 3:
                    # if it is the exit point - mark exit
                    string_to_print += " " + self.board[row][col] + " Exit"
                elif col == (self.__board_width - 1):
                    # if it is the end of a row and there's no exit- mark as #
                    string_to_print += " " + self.board[row][col] + " # "
                else:  # if it is not the exit point and not the end of a row
                    string_to_print += " " + self.board[row][col]
            string_to_print += "\n"  # do down a line after every row
        return string_to_print

    def cell_list(self):
        """ This function returns the coordinates of cells in this board
        :return: list of coordinates
        """
        # In this board, returns a list containing the cells in the square
        # from (0,0) to (6,6) and the target cell (3,7)
        cell_lst = []
        
        # append each cell coordination in board to lst:
        for row in range(self.__board_height):
            for col in range(self.__board_width):
                cell_lst.append((row, col))
        
        cell_lst.append(self.TARGET_CELL)  # append target cell to lst
        
        # now all valid cells are in cell_lst
        return cell_lst
    
    def __is_cell_valid(self, cell):
        """receives a tuple of ints (row, col).
        if cell is empty - return True
        if cell is not empty or not in board - return False
        """
        row, col = cell
 
        if cell not in self.cell_list():  # if cell is not in board
            return False
        if self.board[row][col] == self.EMPTY_CELL:
            return True
        else:
            return False
        
    def possible_moves(self):
        """ This function returns the legal moves of all cars in this board
        :return: list of tuples of the form (name,movekey,description)
                 representing legal moves"""
        # [('O','d',"some description"),('R','r',"some description"),('O',
        # 'u',"some description")]
        res_lst = []

        for car in self.__car_dict.values():  # go over all cars in dicts
            possible_move_dict = car.possible_moves()
            # dict with all possible moves for this specific car_name
            for movekey in possible_move_dict:
                # for each possible move of this car
                # if move is valid for car - check if required cell is empty
                move_req_lst = car.movement_requirements(movekey)
                # list of tuples (cells) we want to check for possible moves
                
                for cell in move_req_lst:
                    if self.__is_cell_valid(cell):
                        # if cell is empty -
                        description = possible_move_dict.get(movekey, None)
                        res_lst.append((car, movekey, description))
        
        return res_lst
    
    def target_location(self):
        """
        This function returns the coordinates of the location which is to be
        filled for victory.
        :return: (row,col) of goal location
        """
        return self.TARGET_CELL
        
    def cell_content(self, coordinate):
        """
        Checks if the given coordinates are empty.
        :param coordinate: tuple of (row,col) of the coordinate to check
        :return: The name if the car in coordinate, None if empty
        """
        row, col = coordinate  # unpack tuple
        if self.board[row][col] == self.TARGET_CELL_START_VALUE:
            return None
        elif self.board[row][col] == self.EMPTY_CELL:
            # if the cell in board is empty - return None
            return None
        else:  # the cell is not empty
            car_in_cell = self.board[row][col]  # set which car is in cell
            return car_in_cell  # return name of the car in cell

    def __is_car_on_board(self, car):
        """checks if car is on board.
         i
         if so - return True, if not, return False"""
         
        car_name = car.get_name()
        
        if car_name in self.__car_dict:
            return True
        else:
            return False

            
    def add_car(self, car):
        """
        Adds a car to the game.
        :param car: car object of car to add
        :return: True upon success. False if failed
        """
        # Remember to consider all the reasons adding a car can fail.
        # You may assume the car is a legal car object following the API.
        car_name = car.get_name()
        if self.__is_car_on_board(car):
            # if car's on board already, it cannot be added
            return False

        car_places_in_board = car.car_coordinates()
        
        # verify car coordianates are in board
        for cord in car_places_in_board:
            if cord[0] not in self.VAILD_LOCATION or cord[1] not in \
                    self.VAILD_LOCATION:
                # if cords are not in board
                return False
        
        # verify coordinates of car are empty
        for loc in car_places_in_board:
            if self.cell_content(loc) is not None:
                # if cell is not empty, we cannot add car to board
                return False
            
        # we can place car in board -
        # 1. add car to car_dict:
        self.__car_dict[car_name] = car
    
        # 2. update board
        for cord in car_places_in_board:
            # change empty cells to car_name
            row, col = cord  # unpack tuple
            self.board[row][col] = car_name  # replace with car's name


        # since car was added to the game, return True
        return True

    # def __is_car_on_board(self, car):
    #     car_name = car.get_name()
    #     car_placement = car.car_coordinates()  # lst of coordinates
    #     if car_name in self.board:
    #         return False
    #     return True

    def __change_board(self, car_to_move, cords, movekey, list_of_cords):
        """input - car_to_move - object of type Car(), new_car_head -
        location, movekey.
        :return updated board with car on it, true or false"""
    
        if car_to_move.move(movekey):  # if move is valid for car
            if movekey == 'l' or movekey == 'u':
                # if movekey is l or u -
                # set car's name on board in place cord
                #  set last cord in list_of_cords on board to be empty
                self.board[cords[0][0]][cords[0][1]] = car_to_move.get_name()
                self.board[list_of_cords[-1][0]][
                    list_of_cords[-1][1]] = self.EMPTY_CELL
            if movekey == 'r' or movekey == 'd':
                # if movekey is r or d -
                # set car's name on board in place cord
                #  set first cord in list_of_cords on board to be empty
                self.board[cords[0][0]][cords[0][1]] = car_to_move.get_name()
                self.board[list_of_cords[0][0]][
                    list_of_cords[0][1]] = self.EMPTY_CELL
            return True
        else:
            return False

    def move_car(self, name, movekey):
        """
        moves car one step in given direction.
        :param name: name of the car to move
        :param movekey: Key of move in car to activate
        :return: True upon success, False otherwise
        """
        if name not in self.__car_dict:  # if car doesn't exist in car_dict
            return False
        
        car_to_move = self.__car_dict.get(name, None)  # check which car is it
        # and set car object as car_to_move
        
        cords = car_to_move.movement_requirements(movekey)
        # a tuple (row, col) - the cell we want to move to
        # that must be empty in order for car to be able to move
        
        possible_move_dict = car_to_move.possible_moves()
        # dict of possible more for car_to_move
        
        list_of_cords = car_to_move.car_coordinates()  # lst of all cords of car
        
        if movekey not in possible_move_dict:
            #if movekey is not one of the car's possible moves -
            return False
        
        for cord in cords:
            if (self.cell_content(cord) is not None) \
                    or cord not in self.cell_list():
                # if cell is not empty
                # or is cord not in board - return False
                return False
        # if valid and we can move car - update board
        res = self.__change_board(car_to_move, cords, movekey, list_of_cords)
        return res

