

def print_to_n(n):
    """func input is an integer >= 1.
    func counts up - prints out all ints from 1 to n """
    if n >= 1:
        print_to_n(n-1)
        print(n)
    

def print_reversed(n):
    """ func input is an integer >=1
    func counts down - prints out all ints from n to 1 """

    if n >= 1:
        print(n)
        print_reversed(n -1)


def has_divisor_smaller_than(n, i):
    """input are 2 int.
    return if n has a smaller divider than i, different than 1 """
    if i == 1:
        return True
        # then the num is prime
    if (n % i) == 0:
        # if n%i == 0 it has a divider smaller then original i
        return False # since it has a divider smaller then i it is *not* prime
    return has_divisor_smaller_than(n, i-1)


def is_prime(n):
    """ input - int,
    output is a bool regarging to if this n is prime- True or False"""
    # if n is 1 or negative for sure num is not prime - return False
    if n <= 1:
        return False
    # call func has_divisor_smaller than - and return it's boolean value
    # start check if num n has a divisor smaller then itself (meanning - (
    # n-1) )
    return has_divisor_smaller_than(n, n-1)


def factorial(n):
    """ calc the factorial value of n. assuming n is an int >= 0"""
    if n < 2:
        return 1
    else:
        return n * factorial(n-1)
    
    
def exp_n_x(n, x):
    """ input - x is a float, n int n>0
    calc the exponential sum of (x**i)/(i!) for i=0 to i=n"""
    if n == 0:
        return 1
    else:
        return x**n / factorial(n) + exp_n_x(n-1, x)


def play_hanoi(hanoi, n, src, dest, temp):
    """ solves game hanoi towers with graphic agr 'hanoi' """
    if n <= 0:
        return
    if n == 1:
        hanoi.move(src, dest)
    if n > 1:
        # move n-1 disks from src to temp
        play_hanoi(hanoi, n-1, src, temp, dest)
        # move last disk from src to dest:
        hanoi.move(src, dest)
        # move n - 1 disks from temp to dest
        play_hanoi(hanoi, n-1, temp, dest, src)
    
    
def print_sequence_helper(char_lst, n, current_word):
    """input -  char_list and an int and a str (default - empty str)
    output - prints out all combinations for in len(n) of chars from list,
    when same char can appear more then once"""
    for char in char_lst:
        # base case
        if n == len(current_word + char):
            # n is max len of word
            print(current_word + char)
        else:
            print_sequence_helper(char_lst, n, current_word + char)


def print_sequences(char_list, n):
    """input -  char_list and an int
    output - prints out all combinations for in len(n) of chars from list,
    when same char can appear more then once"""
    
    if n == 0:
        print()
    current_word = ""
    print_sequence_helper(char_list, n, current_word)
    return


def no_repetition_helper(char_list, n, current_word=""):
    """  input - char_list , n - len of word func would print out, an empty str
    output - prints out comp"""
    for char in char_list:
        if char in current_word:
            continue
        if n == len(current_word + char):
            print(current_word + char)
        else:
            no_repetition_helper(char_list, n, current_word + char)


def print_no_repetition_sequences(char_list, n):
    """input - list of charactors, n - int
    func prints out all combanation for chars in list when char cannot
    appear more then once in a word"""
    no_repetition_helper(char_list, n)


def parentheses_helper(str, num_open, num_close, new_list):
    """ input - a string, num_open - int, num_close - int, a list
     output - list of lists (updated list with all options for correct
     parentheses combination) """
    
    if num_open == 0 and num_close == 0:
        # if we are out of parentheses (open and close) - we ran our of
        # options so we would append the str we have so far to new list
        new_list.append(str)
    
    elif num_open == num_close:
        # if the num of close and open are the same, it means we closed
        # every option we had so now we can only open new ones,
        # unless we would print a false statement
        parentheses_helper(str + "(", num_open - 1, num_close, new_list)
    
    # if there are less open ones:
    elif num_open < num_close:
        if num_open > 0:
            #
            parentheses_helper(str + "(", num_open-1, num_close, new_list)
        # happens when there there are 0 open "(" and we need to close them
        parentheses_helper(str + ")", num_open, num_close-1, new_list)


def parentheses(n):
    """ input: - n - an int
    :return a list with correct possibilities
    func recieves an int and prints out the possible
    methematical correct parentheses combination in a list, when every item
    is a possibility"""
    new_lst = []
    parentheses_helper("", n, n, new_lst)
    return new_lst


def helper_up_and_right(string, k, n):
    """ input: n, k - both int
    assuming we are on a grid at (0,0).
    func prints out the possible
    moves we can make in order to get to (n,k),
    when n is number of steps right and k is num of steps up the grid"""
    # k is number of times we can moves right
    # n is number of times we can moves up
    if k == 0:
        # if i have 0 moves up left - move only right
        for i in range(n):
            string = string + "r"
        print(string)
    elif n == 0:
        # if i have 0 moves right left - move only up
        for i in range(k):
            string = string + "u"
        print(string)
    else:
        # call func with str + u,
        # so we have one less up moves - subtract 1 from k
        helper_up_and_right(string + "u", k-1, n)
        # call func with str + r
        # so we have one less right moves - subtract 1 from n
        helper_up_and_right(string + "r", k, n-1)


def up_and_right(n, k):
    """ input: n, k - both int
    assuming we are on a grid at (0,0).
    func prints out the possible moves we can make in order to get to (n,k),
    when n is number of steps right and k is num of steps up the grid"""

    if k == 0 and n == 0:
        # if we k,n == 0 there is actually no movement at all - stay in place
        return
    # calling helper func which prints out the possible moves
    helper_up_and_right("", k, n)


def flood_helper(image, y, x):
    """input - image - lists of list, x,y - ints (indicate cordination in
    image
    output - updated image (lists of lists) with '*' """
    if image[y][x] == "*":
        return
    # we cannot be 'out of range' since there is a 'frame' of '*', so once func
    # encounter one of them it returns, if next cell is still valid - it
    # will continue to check the next one
    # (assumption is this 'cell' would be 'empty', meaning - "." )
    
    else:
        image[y][x] = "*"
        # call function with one move - each call will check if next cell is
        # valid, if so it will replace it with "*"
        # move one cell up
        flood_helper(image, y + 1, x)
        # move one cell down
        flood_helper(image, y - 1, x)
        # move one cell right
        flood_helper(image, y, x + 1)
        # move one cell left
        flood_helper(image, y, x - 1)
        

def flood_fill(image, start):
    """input - image is list of lists with "*" or "." as items.
     output - updated image """
    # unpack tuple where first index refers to row (y)
    # and 2nd index refers to column (x) in image
    y, x = start
    # calling func to update image
    flood_helper(image, y, x)
    return 


image1 = [['*', '*', '*', '*', '*'],
          ['*', '*', '*', '.', '*'],
          ['*', '*', '*', '.', '*'],
          ['*', '*', '*', '*', '*']]

result = [['*', '*', '*', '*', '*'],
          ['*', '*', '*', '.', '*'],
          ['*', '*', '*', '.', '*'],
          ['*', '*', '*', '*', '*']]
start1 = (1, 1)