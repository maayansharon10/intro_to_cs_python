import copy

######################## part 1 soduko solver  ###########################


def is_valid_in_row(board, k, y, n):
    """func checks if k (int) is valid in row of cell [y][x]"""
    # y >= 0 : num of rows
    for x in range(n):
        cell = board[y][x]
        if k == cell:
            return False
    return True


def is_valid_in_cul(board, k, x, n):
    """checks if k is in cul """
    for y in range(n):
        cell = board[y][x]
        if k == cell:
            return False
    return True


def is_valid_in_square(board, k, row, column, n):
    """func checks if k is in square of size the root of n"""
    col_place_start = column - int((column % (n ** 0.5)))
    # in which col we want to start
    col_place_end = col_place_start + int(n ** 0.5)
    # in which col we want to end
    row_place_start = row - int((row % (n ** 0.5)))
    # in which row we want to start
    row_place_end = row_place_start + int(n ** 0.5)
    # in which row we want to end
    
    # now check in desired square if k in square.
    # if so - it is not valid there so return False
    for row_in_board in range(row_place_start, row_place_end):
        for col_in_board in range(col_place_start, col_place_end):
            if k == board[row_in_board][col_in_board]:
                return False
    # k is valid in desired square - return True
    return True


def is_k_valid(board, k, column, row, n):
    """func checks if the num k is valid in board of size n, in cell [y][x]
     and returns True or False"""
    
    if is_valid_in_row(board, k, row, n) \
            and is_valid_in_cul(board, k, column,n) \
            and is_valid_in_square(
        board, k, row, column, n):
        # if k is valid in row, cul and squere of size root of n - it is valid
        return True
    else:  # k was found not valid for cell
        return False


def sudoku(board, i, n):
    """func solves suduko.
    inputs are: board - list of lists of mat of n*n cells
    n - size of length and width of board
    i - the cell of board from 0 to n-1.
    :return True, and board is updated with solution if there is one.
            False - and then board stayss as is if"""

    if i >= n * n:
        return True
    x = int(i % n)  # find place in column
    y = int(i / n)  # find place in row
    if board[y][x] != 0:  # if cell is not empty
        return sudoku(board, i + 1, n)  # skip and continue to check next cell
    else:
        for k in range(1, n + 1):  # for ints from 1 to n
            if is_k_valid(board, k, x, y, n):  # check if num is
                # valid for cell
                board[y][x] = k  # if valid, set in cell
                
                if sudoku(board, i + 1, n):  # continue and check next cell in
                    #  board
                    return True
                
                # Revert before trying the next number - so the board
                # goes back to default when there is no solution
                board[y][x] = 0
        
        # I tried all the options, non of them worked
        return False


# main sudoku function
def solve_sudoku(board):
    """func solvoes sodoko
    :return True, and board is updated with solution if there is one.
    False - and then board stays as is """
    
    n = len(board)  # check what board size is . assume length = width
    
    return sudoku(board, 0, n)
    # start solving board of size board_size  # from first cell (num 0)


#################### part 2 func 1#############################


def print_set(cur_set):
    """func unpack tuple and append all index with value True to list,
    then print list"""
    lst = []
    
    for idx, in_cur_set in enumerate(cur_set):
        if in_cur_set:
            lst.append(idx)
    
    print(lst)


def print_k_subsets_helper(cur_set, k, index, picked):
    """ func prints out all 'good' options for a set of size k of a group {
    0,..,n-1} in a sorted from small to large """
    # base: we picked out k items
    if k == picked:
        print_set(cur_set)
        return
    # if we reached the end of the list, backtrack
    if index == len(cur_set):
        return
    # run on all sets that include this index
    cur_set[index] = True
    print_k_subsets_helper(cur_set, k, index + 1, picked + 1)
    # runs on all sets that include this index
    cur_set[index] = False
    print_k_subsets_helper(cur_set, k, index + 1, picked)


def print_k_subsets(n, k):
    """func prints all sub sets of size k of group 0 to n-1 in a
    sorted way from small to large element if k<= n  (calls sub functions)"""
    if k <= n:
        cur_set = [False] * n
        print_k_subsets_helper(cur_set, k, 0, 0)



######################## part 2 func 2  ###########################
def create_list_of_s(cur_set):
    """func unpacks tuple (index, True/False), when true, append index to
    list. returns list"""
    lst = []
    for idx, cur_in_set in enumerate(cur_set):
        if cur_in_set:
            lst.append(idx)
    return lst


def fill_k_subsets_helper(cur_set, k, index, picked, lst):
    """update lst according to the index and cur_set, so in every sublist
    there's a list with only the valid indexes we need. then call func again
    and backtrack """
    # base: we picked out k items
    if k == picked:
        lst.append(create_list_of_s(cur_set))
        return
    # if we reached the end of the list, backtrack
    if index == len(cur_set):
        return
    # run on all sets that include this index
    cur_set[index] = True
    fill_k_subsets_helper(cur_set, k, index + 1, picked + 1, lst)
    
    # runs on all sets that include this index
    cur_set[index] = False
    fill_k_subsets_helper(cur_set, k, index + 1, picked, lst)


def fill_k_subsets(n, k, lst):
    """get to ints n,k creates a list with all sub sets of size k of 0 to n"""
    if k <= n:
        new_lst = n * [False]
        fill_k_subsets_helper(new_lst, k, 0, 0, lst)


######################## part 2 func 3  ###########################
def helper_return_k_no_args(n, k):
    """creates and returns a list with all options of set of len k from
    elements 0 to n """
    if n == 0:
        return [[]]
    lst = helper_return_k_no_args(n-1, k)
    new_lst = copy.deepcopy(lst)
    for i in range(new_lst):
            new_lst[i].append(n-1)
    return new_lst + lst
    

def return_k_subsets(n, k):
    """picks only good options for lists of size k, append to list and
    returns it so we get a list of lists with each sublist is with k
    different elements """
    lst = helper_return_k_no_args(n, k)
    new_lst =[]
    for element in lst:
        if len(element) == k:
            new_lst.append(element)
    return new_lst

