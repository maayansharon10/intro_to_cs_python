import hangman_helper as hm


def is_user_input_valid(string):
    """ checks if the user input is only a ONE lower case letter."""
    if len(string) != 1:
        return False
    elif string.islower():
        return True
    else:
        return False


def update_word_pattern(word, pattern, letter):
    """update the pattern according to the letter and the word. returns the
    new pattern"""
    current_word_list = list(word)
    current_pattern_list = list(pattern)
    for let1 in range(len(current_word_list)):
        if current_word_list[let1] == letter:
            current_pattern_list[let1] = letter
    pattern = ''.join(current_pattern_list)
    return pattern


def is_letter_already_chosen(user_input, wrong_guess_lst, pattern):
    """check if the letter already exist in pattern"""
    for letter in wrong_guess_lst:
        if user_input == letter:
            return True
    if user_input in pattern:
        return True
    return False


def is_letter_in_pattern(user_input, word):
    """checks if the letter the user chose is in the word"""
    for letter in list(word):
        if user_input == letter:
            return True
    return False


def is_letter_in_wrong_guess_list(word, wrong_guess_lst):
    """check if letter is in wrong guess list and if so - return False"""
    for letter in word:
        if letter in wrong_guess_lst:
            return False  # the word is irrelevant
    return True  # if the word fits the pattern (is not in wrong_guess_lst


def is_letter_in_place_word_list(pattern, word):
    """which letter in pattern is at the exact same place as the woor in
    list if so - return True"""
    lst_pattern = list(pattern)
    word_to_lst = list(word)
    for letter in range(len(lst_pattern)):
        if lst_pattern[letter] == "_":
            continue
        else:
            # letter != "_":
            if lst_pattern[letter] != word_to_lst[letter]:
                return False
                # if there are 2 letter at the same place but not the same
    return True
    # if all letters at the same place are the same


def filter_words_list(word_list, pattern, wrong_guess_lst):
    """receive a list of words, pattern and wrong guess list, output is a
    new list with only the words that with the same len, same letters with
    do not include any of the words in wrong quess list"""
    filtered_list = []
    for word in word_list:
        if len(word) == len(pattern):
            # if the word in the list has the same amount of letter
            if is_letter_in_wrong_guess_list(word, wrong_guess_lst):
                # letters in word are not in wrong guess list
                if is_letter_in_place_word_list(pattern, word):
                    filtered_list.append(word)
    return filtered_list


def end_game_msg(pattern, word):
    if "_" in pattern:
        return hm.LOSS_MSG + word
    else:
        return hm.WIN_MSG


def run_single_game(word_list):
    wrong_guess_lst = []
    error_count = 0
    word = hm.get_random_word(word_list)
    pattern = (len(word) * "_")
    display_user_msg = hm.DEFAULT_MSG
    ask_play = False
    while word != pattern and error_count < \
            hm.MAX_ERRORS:
        # while word and pattern are not the same - continue for
        # another round
        
        hm.display_state(pattern, error_count, wrong_guess_lst,
                         display_user_msg, ask_play)
        # should be in while loop or outside??
        user_input_type, user_input = hm.get_input()
        if user_input_type == hm.LETTER:
            if not is_user_input_valid(user_input):
                # if the user_input is not one letter of a-z -
                #  display non valid
                display_user_msg = hm.NON_VALID_MSG
                continue
            
            # user input is valid
            if is_letter_already_chosen(user_input, wrong_guess_lst, pattern):
                display_user_msg = hm.ALREADY_CHOSEN_MSG + user_input
                continue
            
            # no duplicate input
            if is_letter_in_pattern(user_input, word):
                # if the letter the user chose is in word -
                pattern = update_word_pattern(word, pattern,
                                              user_input)
                display_user_msg = hm.DEFAULT_MSG
            else:
                # the letter chosen is not in word
                error_count = error_count + 1
                wrong_guess_lst.append(user_input)
                display_user_msg = hm.DEFAULT_MSG
        elif user_input_type == hm.HINT:
            filtered_list = filter_words_list(word_list, pattern,
                                              wrong_guess_lst)
            # brings back a list with word at same len, have the same letters
            #  as pattern at same place and do not have any of the letters
            # in the wrong_guess_lst
            
            hint_letter = choose_letter(filtered_list, pattern)

            display_user_msg = hm.HINT_MSG + hint_letter
            hm.display_state(pattern, error_count, wrong_guess_lst,
                             display_user_msg, ask_play)
    display_user_msg = end_game_msg(pattern, word)
    hm.display_state(pattern, error_count, wrong_guess_lst,
                     display_user_msg, ask_play = True)


def make_letter_histogram(words, pattern):
    """receive a list of words as input, and current pattern. output is the
        a dict of hisogram of letters(key = letter, value = num of time it
        appear in lst"""
    letter_dict = dict()
    for word in words:
        # if the word in the list has the same amount of letter
        for letter in word:
            if letter not in pattern:
                letter_dict[letter] = letter_dict.get(letter, 0) + 1
    return letter_dict


def choose_letter(words, pattern):
    """receive a list of words as input, and current pattern. output is the
    letter (str) which appeares the most in this list"""
    letter_histogram = make_letter_histogram(words, pattern)
    biggest_value = 0
    for key, value in letter_histogram.items():
        if value >= biggest_value:
            biggest_value = value
            biggest_letter = key
    return biggest_letter


def main():
    word_list = hm.load_words()
    run_single_game(word_list)
    user_input_type, user_input = hm.get_input()
    while (user_input_type, user_input) == (hm.PLAY_AGAIN, True):
        run_single_game(word_list)
        user_input_type, user_input = hm.get_input()
        


if __name__ == "__main__":
    hm.start_gui_and_call_main(main)
    hm.close_gui()
