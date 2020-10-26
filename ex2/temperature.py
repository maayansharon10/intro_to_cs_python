
def is_it_summer_yet(best_temp, first_temp, second_temp, third_temp):
    """ the function recieves 4 arguments - the first is the
    'best temperature' which is the pre-condition. function will
    return True when the 2nd and 3rd and 4th arg are larger then
    best_temp. Otherwise will return False """
    if (first_temp > best_temp) and (second_temp > best_temp):
        return True
    elif (first_temp > best_temp) and (third_temp > best_temp):
        return True
    elif (second_temp > best_temp) and (third_temp > best_temp):
        return True
    else:
        return False
