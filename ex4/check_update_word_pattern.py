import hangman as hm_ex


def check_for_update_word_pattern():
    result = True
    if hm_ex.update_word_pattern('ppppp', '_____', 'p') == 'ppppp':
        # in case all letters needed to be updated are the same one after
        # the other
        result = True
        print("if1 = true")
    else:
        result = False
    
    if hm_ex.update_word_pattern('plplp', '_____', 'l') == '_l_l_':
        # in case several letters needed to be updated are the same are not
        # next to each other
        result = True
    else:
        result = False

    if hm_ex.update_word_pattern('pabcdefp', '_abcdef_', 'p') == 'pabcdefp':
        # in case the word is very long and the letter we need to update is
        # the last one
        result = True
    else:
        result = False

    if hm_ex.update_word_pattern('apple', 'a__l_', 'j') == 'a__l_':
        # in case the letter is not in word and pattern should not be updated
        result = True
    else:
        result = False
    
    if result is True:
        return result
    else:
        return result


if __name__ == "__main__":
    check_for_update_word_pattern()