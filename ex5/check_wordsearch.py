import wordsearch as ws

matrix_1 = [['a', 'a', 'a', 'a', 'a'],
            ['b', 'b', 'b', 'b', 'b'],
            ['a', 'a', 'a', 'a', 'a'],
            ['b', 'b', 'b', 'b', 'b'],
            ['a', 'a', 'a', 'a', '']]
matrix_2 = [['a', 'a', 'a', 'a', 'a', 'c', 'v', 'g', 't', 'w'],
            ['b', 'b', 'b', 'b', 'b', 'e', 'c', 'd', 's', 's'],
            ['a', 'a', 'a', 'a', 'a', 'c', 'd', 'f', 'r', 'e'],
            ['b', 'b', 'b', 'h', 'e', 'l', 'l', 'o', 'j', 'v'],
            ['a', 'a', 'a', 'a', 'a', 'l', 'o', 'k', 'x', 'z'],
            ['y', 'u', 'i', 'w', 'e', 's', 'd', 't', 'c', 's'],
            ['z', 'c', 'r', 'e', 's', 'd', 'd', 'v', 'r', 'a'],
            ['e', 't', 'y', 'u', 'd', 's', 'c', 'w', 'x', 's'],
            ['e', 't', 'y', 'u', 'f', 'a', 'q', 'z', 'x', 'c'],
            ['o', 'p', 'l', 'k', 'n', 'h', 'b', 'v', 'r', '']]
matrix_3 = [['a', 'a', 'a', 'a', 'a', 'c', 'v', 'g', 't', 'w'],
            ['b', 'b', 'b', 'b', 'b', 'e', 'c', 'd', 's', 's'],
            ['a', 'e', 'a', 'a', 'a', 'c', 'd', 'f', 'r', 'e'],
            ['a', 'a', 'a', 'a', 'a', 'l', 'o', 'k', 'x', 'z'],
            ['y', 'u', 'i', 'u', 'e', 's', 'd', 't', 'c', 's'],
            ['z', 'c', 'r', 'e', 't', 'd', 'd', 'v', 'r', 'a'],
            ['e', 't', 'y', 'u', 'd', 'i', 'c', 'w', 'x', 's'],
            ['e', 't', 'y', 'u', 'f', 'a', 'f', 'z', 'x', 'c'],
            ['b', 'e', 'a', 'u', 't', 'i', 'f', 'u', 'l', 'v'],
            ['o', 'p', 'l', 'k', 'n', 'h', 'b', 'v', 'l', '']]


def check_count_word_in_mat():
    result = True
    # try all directions for a matrix with only 2 letters (check repetition)
    if ws.count_word_in_mat(matrix_1, 'udlrzxwy', 2, 1, 'ba', 5, 5) != 6:
        # out put suppose to be 6
        result = False
        print("repetition failed")
    else:
        print("repetition success")
        
    # func only checks direction once, even if appears in input several times
    if ws.count_word_in_mat(matrix_1, 'dddddd', 2, 1, 'ba', 5, 5) != 1:
        # output suppose to be 1
        result = False
        print("multiple times same direction failed")
    else:
        print("multiple times same direction success")
    
    # func recognizes a word in a large matrix:
    if ws.count_word_in_mat(matrix_2, 'r', 3, 3, 'hello', 10, 10) != 1:
        # output suppose to be 1
        result = False
        print("large matrix, word in middle failed")
    else:
        print("large matrix, word in middle success")
        
    # func recognizes a long word in a large matrix, in  diagonal vector
    if ws.count_word_in_mat(matrix_3, 'y', 0, 1, 'beautiful', 10, 10) != 1:
        # output suppose to be 1
        result = False
        print("large matrix, diagonal long word failed")
    else:
        print("large matrix, diagonal long word success")
    
    # check if it can recognize a word with only one letter
    if ws.count_word_in_mat(matrix_3, 'l', 0, 0, 'a', 10, 10) != 1:
        # output suppose to be 1
        result = False
        print("large matrix, one letter word failed")
    else:
        print("large matrix, one letter word success")
    return result

print(check_count_word_in_mat())