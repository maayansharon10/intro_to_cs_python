import random


class Board:
    EMPTY_CELL = 0

    def __init__(self, num_rows=6, num_cols=7):
        self.set_len = 4
        board = []
        self.__board_height = num_rows
        self.__board_width = num_cols
        # create board :
        for row in range(self.__board_height):
            row_lst = []
            for col in range(self.__board_width):
                row_lst.append(Board.EMPTY_CELL)
            board.append(row_lst)
        self.board = board
        self.winning_set = [[-1, -1], [-1, -1], [-1, -1], [-1, -1]]

        # list of disks:
        self.lst_of_disks = []
        # list of locations of disks on board
        self.lst_of_locs = []
        # dictionary of locations for each player {player : locations of
        # disks of this player as tuples)
        self.disk_dict = dict()

    def __str__(self):
        string_to_print = ""
        for row in range(self.__board_height):
            string_to_print += "row" + str(row) + ":"
            for col in range(self.__board_width):
                string_to_print += " " + str(self.board[row][col])
            string_to_print += "\n"  # do down a line after every row
        return string_to_print

    def get_num_of_cells_in_board(self):
        """:return num of cells in board (int)"""
        return self.__board_height * self.__board_width

    def who_in_this_cell(self, row, col):
        """func return's the current cell value
        :param row
        :param col
        :return the current disk in cell - int represent a player.
        if there's no player in cell : 0
        if cell doesn't exist - return -1 """

        try:

            current_cell = self.board[row][col]
            return current_cell

        except:
            IndexError("Illegal location")

    def can_add_disk_at_col(self, col):
        """checks if disk can be added at this call.
        :param col - int
        :return True upon success, False otherwise"""

        # if col is in range and the the highest row is not full - we can
        # add a disk

        if col <= self.__board_width:
            if self.board[0][col] == 0:
                return True

        raise IndexError("illegal move.")  # Col is full or out of board

    def add_disk_to_board(self, col, disk):
        """add disk to board at column.
        :param col - int
        :param disk - 1 letter
        :return True upon success, False otherwise"""

        # add to board:
        # check from the bottom up:
        # once hit 0 - place disk in cell and return
        if self.can_add_disk_at_col(col):  # Might raise an exception!
            for row in range(self.__board_height - 1, -1, -1):
                if self.board[row][col] != 0:  # if cell is not empty,
                    # check the one above it
                    continue
                else:
                    self.board[row][col] = disk  # if cell is empty -
                    # place disk
                    # we added disk to board. update list_of_disks:
                    self.lst_of_disks.append(disk)
                    self.lst_of_locs.append((row, col))
                    break

    def get_all_valid_col(self):
        """func returns a list of all valid columns in board (ones we can
        add disks to)"""
        # create a list of all col in board -
        col_options = list(range(self.__board_width))
        valid_cols = []  # valid columns

        for col in col_options:  # go through all col in board
            try:
                if self.can_add_disk_at_col(col):  # if col is valid
                    valid_cols.append(col)
            except:
                IndexError("Illegal Move.")  # ignore wrong moves.

        return valid_cols

    def pick_random_col(self):
        """func picks random col in which we can add disk. return num of
        valid random col"""
        col_options = list(range(self.__board_width))
        chosen_col_valid = False
        while not chosen_col_valid:
            random_col = random.choice(col_options)
            # check if we can add disk to random column:
            chosen_col_valid = self.can_add_disk_at_col(random_col)
            # returns true of false
        # a valid column was found -
        return chosen_col_valid

    #################  funcs searching for victory status ########################

    def is_board_full(self):
        """ check if board is full with disks
        :return True or false"""

        there_is_empty_cell = False
        # check if the highest row is all full:
        for cell in self.board[0]:
            if cell == 0:  # if there's one empty cell - then board is not full
                there_is_empty_cell = True

        if there_is_empty_cell:  # there's one empty cell so board is not full
            return False
        else:
            return True  # board is full

    def is_there_4_in_a_row(self, player_num):
        """ func search for 4 in a row
        :param player_num - int
        :return: True if there is, False of there's not"""
        set_for_search = str(player_num) * 4  # four of the same disk
        board_length = self.__board_height
        board_width = self.__board_width
        set_exist = False
        # check when we find the first disk of current player on board
        for row in range(board_length):
            for col in range(board_width):
                if set_for_search[0] == str(self.board[row][col]):
                    # go through all letters in mat. of there's a match
                    # between the first letter of the word and letter in mat.
                    # if we have a match - check according to the directions,
                    # if the word exists.
                    set_exist = self.search_set_in_board(col, row,
                                                         set_for_search,
                                                         board_length,
                                                         board_width)
                    if set_exist:  # if we found a set - return
                        return set_exist
                    # if not - keep cheeking
        return set_exist

    def search_set_in_board(self, x, y, set_to_search, mat_length, mat_width):
        """if we got a match, meaning we found the first disk of a
        potentional set, in board,
        :return True if set appears at least one time in any of the possible
        directions. """
        directions_dicts = {'u': (-1, 0), 'd': (1, 0), 'r': (0, 1),
                            'l': (0, -1), 'w': (-1, 1), 'x': (-1, -1),
                            'y': (1, 1), 'z': (1, -1)}
        # (y,x) a tuple with the directions instructions
        set_len = len(set_to_search)  # the number of cul
        set_exist = False
        chrs_so_far = set()
        for char in directions_dicts:

            if char in chrs_so_far:  # if direction was already checked
                break
            # if the character is the same - move one step in same direction
            #  and add one to i to check next letter in word
            else:
                chrs_so_far.add(char)

            dx = x
            dy = y
            i = 0

            while 0 <= dx < mat_width and 0 <= dy < mat_length and i <= set_len:
                # we want to check if the next chr in the set_for_search
                # matches
                # the n conditions so we won't be out of range for board. also,
                # that we won't continue check up more then num of letter in
                #  set.
                if set_to_search[i] != str(self.board[dy][dx]):
                    break
                # if the character is the same - move one step in same
                # direction
                #  and add one to i to check next letter in word
                self.winning_set[i] = [dy, dx]
                dy += directions_dicts[char][0]
                dx += directions_dicts[char][1]
                i += 1

                if i == set_len:  # if the whole word is in matrix in this dir
                    set_exist = True
                    return set_exist
        return set_exist

    #########################################################################

    # simillar but *different* functions aiming to help ai player search on
    #  board return values are different and using only when ai player try to
    #  find best next move.

    def is_there_x_in_a_row(self, player_num, x):
        """ func search for x in a row of player_num. uses search sets for
        ai as helper function
        :param player_num - int
        :param x -int
        :return: int - num of times set appears on board. 0 if None"""
        set_for_search = str(player_num) * x  # x of the same disk
        board_length = self.__board_height
        board_width = self.__board_width
        counter = 0
        # check when we find the first disk of current player on board
        for row in range(board_length):
            for col in range(board_width):
                if set_for_search[0] == str(self.board[row][col]):
                    # go through all letters in mat. of there's a match
                    # between the first letter of the word and letter in mat.
                    # check according to the directions if the word exists.
                    set_exist = self.search_sets_for_ai(col, row,
                                                        set_for_search,
                                                        board_length,
                                                        board_width)
                    if set_exist:  # if we found a set - return
                        counter += 1
                    # if not - keep cheeking
        return counter

    def search_sets_for_ai(self, x, y, set_to_search, mat_length, mat_width):
        """if we got a match, meaning we found the first disk of a
        potentional set, in board,
        :return True if set appears at least one time in any of the possible
        directions. """
        directions_dicts = {'u': (-1, 0), 'd': (1, 0), 'r': (0, 1),
                            'l': (0, -1), 'w': (-1, 1), 'x': (-1, -1),
                            'y': (1, 1), 'z': (1, -1)}
        # (y,x) a tuple with the directions instructions
        set_len = len(set_to_search)  # the number of cul
        chrs_so_far = set()
        counter = 0
        for char in directions_dicts:

            if char in chrs_so_far:  # if direction was already checked
                break
            # if the character is the same - move one step in same direction
            #  and add one to i to check next letter in word
            else:
                chrs_so_far.add(char)

            dx = x
            dy = y
            i = 0

            while 0 <= dx < mat_width and 0 <= dy < mat_length and i <= \
                    set_len:
                # we want to check if the next chr in the set_for_search
                # matches
                # the n conditions so we won't be out of range for board. also,
                # that we won't continue check up more then num of letter in
                #  set.
                if set_to_search[i] != str(self.board[dy][dx]):
                    break
                # if the character is the same - move one step in same
                # direction
                #  and add one to i to check next letter in word
                dy += directions_dicts[char][0]
                dx += directions_dicts[char][1]
                i += 1
                # if the whole word is in matrix in the right direction,
                # add+1 to counter
                if i == set_len:
                    counter += 1
                    i = 0
                    continue

        return counter
