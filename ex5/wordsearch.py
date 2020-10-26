import sys
import os.path


def check_if_file_exist(file):
    """check if arg is an existing file. input - a string with name of the
    file. output -True if file exists/False if not"""
    if os.path.exists(file):
        return True
    else:
        return False


def check_if_directions_is_valid(directions):
    """check if directions are valid. input - arg[4] - directions, output -
    if the direction is valid (true), if not (false)"""
    direction_types_lst = ['u', 'd', 'r', 'l', 'w', 'x', 'y', 'z']
    directions_lst = list(directions)
    result = True
    for letter in directions_lst:
        if letter not in direction_types_lst:
            result = False
    return result


def check_input_args(args):
    """check if input is valid, if so, returns None if not, returns False"""
    # check number of arg from command line is valid
    if len(args) != 5:
        return "number of arg is not valid (not 5)"
    # check files exist, if one of them doesn't - return false
    if check_if_file_exist(args[1]) is False:
        return "args[1] (word_file.txt) does not exist"
    if check_if_file_exist(args[2]) is False:
        return "args[2] (mat.txt) does not exist"
    # check if directions input is valid, if not - return False:
    if check_if_directions_is_valid(args[4]) is False:
        return "arg[4] -directions- is not valid"
    return None


def read_wordlist_file(filename):
    """ receives a string with file name, open file and put the words in a list
    input - a string with file name.
    output - a list with the words in the file"""
    words_as_list = []
    with open(filename) as file_wordlist:
        for line in file_wordlist:
            word = line.strip()
            if word.isalpha():
                # if line indid consist only from valid letters = appand to lst
                words_as_list.append(line.strip())
    return words_as_list


def read_matrix_file(filename):
    """receive mat from type txt and output is a list in list - every list
    is a line of letters from mat """
    lst_of_mat = []
    with open(filename) as file_mat:
        for line in file_mat:
            # add every line not including the last note since it is "\n"
            lst_of_mat.append(line[:-1].split(','))
    return lst_of_mat


def count_word_in_mat(matrix, directions, x, y, word, mat_length, mat_width):
    """if we got a match, meaning we found the first letter of the word in
    matrix, this func's input is the matrix, the location in mat, x and y,
    the word we search and the length and width of the mat so we won't be
    out of range. output is the num of times word appears in mat from this
    location and those directions. """
    directions_dicts = {'u': (-1, 0), 'd': (1, 0), 'r': (0, 1), 'l': (0, -1),
                        'w': (-1, 1), 'x': (-1, -1), 'y': (1, 1), 'z': (1, -1)}
    # (y,x) a tuple with the directions instructions
    word_len = len(word)
    # the number of cul
    counter_word = 0
    chrs_so_far = set()
    for chr in directions:
        # if direction was already checked - if so - break
        if chr in chrs_so_far:
            break
        else:
            chrs_so_far.add(chr)
        # since we already know that the first chr is a match
        # we will check first anyway in case it's a one character word
        dx = x
        dy = y
        i = 0
        
        while 0 <= dx < mat_width and 0 <= dy < mat_length and i < word_len:
            # we want to check if the next chr in the word matches the n
            # conditions so we won't be out of range for mat. also, that we
            # won't continue check up more then num of letter in word.
            if word[i] != matrix[dy][dx]:
                break
            # if the character is the same - move one step in same direction
            #  and add one to i to check next letter in word
            dy += directions_dicts[chr][0]
            dx += directions_dicts[chr][1]
            i += 1
            # if the whole word is in matrix in the right direction,
            # add+1 to counter
            if i == word_len:
                counter_word += 1
    return counter_word


def find_words_in_matrix(word_list, matrix, directions):
    """
    :param word_list:
    :param matrix:
    :param directions:
    :return: lst of tuple (word, number of times it appeared)
    """
    mat_length = len(matrix)
    mat_width = 0
    words_in_mat = {}
    if mat_length > 0:
        mat_width = len(matrix[0])
    # check when we have a match first letter in word from list and one of
    # the chr in the matrix, then if it finds one, it finds the number of
    # times it appear and put it in a list
    for y in range(mat_length):
        for x in range(mat_width):
            for word in word_list:
                if word[0] == matrix[y][x]:
                    # go through all letters in mat. of there's a match
                    # between the first letter of the word and letter in mat.
                    # if we have a match - check according to the directions,
                    # if the word exists.
                    counter = count_word_in_mat(matrix, directions, x, y, word,
                                                mat_length, mat_width)
                    if counter != 0:
                        # if the word exists - add to dict key = word,
                        # value = number or times it appeared.
                        words_in_mat[word] = words_in_mat.get(word,
                                                              0) + counter
    # change the dict to list of tuple
    lst_of_tuples = organize_result_lst(words_in_mat)
    return lst_of_tuples


def create_result_list(dict_words_in_mat):
    """func receives dictionary with all the result. output is a list with
    couple of tuples in the order"""
    tuple_lst = []
    for key in dict_words_in_mat.keys():
        tuple_lst.append((key, dict_words_in_mat[key]))
    return tuple_lst


def organize_result_lst(dict_words_in_mat):
    """sorting a list of tuples alphabetically
    input - dict with word in keys. output - a sorted list"""
    tuple_lst = create_result_list(dict_words_in_mat)
    new_lst = sorted(tuple_lst)
    return new_lst


def write_output_file(results, output_filename):
    """func receives 2 arg - result is a list of pairs (word, count) and
    write it in the output file the pairs in the same order."""
    with open(output_filename, 'w') as f:
        for item in range(len(results)):
            if item == len(results) - 1:
                # in the last row - add (word, val)but do not add "\n"
                f.writelines(results[item][0] + "," + str(results[item][1]))
            else:
                # write in file (word, val) and go down a line
                f.writelines(results[item][0] + "," + str(results[item][1]))
                f.write("\n")
    return output_filename


def main():
    # receive arguments from command line
    args = sys.argv
    # check if arguments are valid, if not, print msg
    all_good = check_input_args(args)
    if all_good:
        print(all_good)
        return
    word_list = read_wordlist_file(args[1])
    matrix = read_matrix_file(args[2])
    output_file = args[3]
    directions = args[4]
    result = find_words_in_matrix(word_list, matrix, directions)
    write_output_file(result, args[3])


if __name__ == '__main__':
    main()