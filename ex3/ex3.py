import math
BOOM_NUMBER = 7


def input_list():
    """ check user_input, convvert to str and append in a list.
    output - a list with user inputs"""
    user_input = True
    user_list = []
    while True:
        user_input = input()
        if user_input == "":
            break
        user_list.append(user_input)
    return user_list


def concat_list(str_list):
    """receives a list of strings as input, coneect them into
    one string and the output is the concatenation"""
    new_str = ""
    for i in range(len(str_list)):
        if i == len(str_list)-1:
            new_str = new_str+str_list[i]
        else:
            new_str = new_str + str_list[i] + " "
    return new_str


def maximum(num_list):
    """input is a list of nums, output is the element with the largest value"""
    if num_list == []:
        return None
    max_up_until_now = num_list[0]
    for element in num_list:
        if max_up_until_now < element:
            max_up_until_now = element
    return max_up_until_now


def shift_cycle(lst_to_shift):
    """shift the list one. input - list, output - list shifted backwards by
    1"""
    # changing lst1
    first_element = lst_to_shift[0]
    del lst_to_shift[0]
    lst_to_shift.append(first_element)
    return lst_to_shift


def cyclic(lst1, lst2):
    """receives 2 lists and return a boolean expression if the 2nd list is
    can be received from the first list by shifting a side by m
    steps (in a
    circular motion"""
    if len(lst1) != len(lst2):
        # in case number of elements in lists are not the same - return False
        return False
    elif lst1 == lst2:
        return True
    else:
        lst_to_check = lst1
        for loop in range(len(lst_to_check)):
            lst_to_check = shift_cycle(lst_to_check)
            if lst2 == lst_to_check:
                return True
        return False



def boom_list(n):
    """func receives an n>0, creates list with 'boom' instead of the digit 7
    or 7 multiply by any number"""
    lst1 = list(range(1, n+1))  # creating a list from 0 to n
    new_list = []  # list we will use for our results
    for number in lst1:
        if number % 7 == 0:
            # can be divided by 7 - change to boom and add to new_list
            number = "boom"
            new_list.append(str(number))
        else:
            # if number does not divided by 7
            # check if number contain the digit 7
            # and if so -num_to_append = True,
            check_number = str(number)
            check_number_list = list(check_number)
            num_to_append = number
            for digit in check_number_list:
                if digit == "7":
                    num_to_append = 'boom'
            new_list.append(str(num_to_append))
    return new_list


def seven_boom(n):
    """7 boom. receives n>0, n is from class int,
    output is a list where all numbers which divide by 7 or
    has the digit 7 in them will be replayed with 'boom' """
    list_with_boom = boom_list(n)
    return list_with_boom


def histogram(n, num_list):
    """A histogram is an accurate representation of the distribution of
     numerical data. input is n of type int>0m and a list of numbers. ourput
     is a list with the number of times each number appeared on origial
     list"""
    histogram_list = [0]*n
    for num in num_list:
        histogram_list[num] = histogram_list[num]+1
    return histogram_list


def is_prime(num):
    """input is a number, if the number is prime it returns True"""
    divide_by = 2
    while divide_by <= math.sqrt (num):
        if num % divide_by == 0:
            return False
        divide_by = divide_by + 1
    return True


def prime_factors(n):
    """ input - a number. output - a list with all the number prime factors"""
    prime_factor_list = []
    if n == 0:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            if is_prime(i):
                while n % i == 0:
                    prime_factor_list.append(i)
                    n = n / i
    if n != 1:
        prime_factor_list.append(int(n))
    return prime_factor_list


def cartesian(lst1, lst2):
    """ input is 2 lists. returns a set (or product set or simply product)
    from multiple sets, also a list """
    lst3 = []
    for i in lst1:
        for j in lst2:
            lst3.append([i, j])
    return lst3


def pairs(num_list, n):
    """function input is a list of numbers and n from type int.
    output is a list of all pairs in length of 2 that their sum == n"""
    pairs_list = []
    
    for num in range(len(num_list)):
        for place in range(num+1, len(num_list)):
            # range is between num+1(so we won't check an option of adding a
            #  number with itself) to len(num_list) so we won't be out of
            # range.
            if num_list[num] + num_list[place] == n:
                pairs_list.append([num_list[place], num_list[num]])
    return pairs_list


