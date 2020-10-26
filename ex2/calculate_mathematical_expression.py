

def calculate_mathematical_expression(num_1, num_2, operator):
    """ a function that asks the user for 2 numbers and an operator,
    then calculates the result."""
    if operator == '+':
        # when the operator is "+" - add
        result_num = num_1 + num_2
    elif operator == '-':
        # when the operator is "-" - subtract
        result_num = num_1 - num_2
    elif operator == '/':
        # when the operator is "/" - divide
        if num_2 == 0:
            # we cannot divide any number by zero, therefore will return None
            return None
        else:
            result_num = num_1 / num_2
    elif operator == '*':
        # When operator "*" - multiply
        result_num = num_1 * num_2
    else:
        # no other operators are allowed in this function
        return None
    return result_num


def calculate_from_string(text):
    """  a function that takes a value from
    calculate_mathematical_expression and """
    # we will split the text received in the function as an argument
    #  in order  to use the 2 num and operator in
    #  the string in the former function.
    new_text = text.split(" ")
    num1 = float(new_text[0])
    operator2= str((new_text[1]))
    num2 = float(new_text[2])
    # using the new numbers and operator in
    # the function calculate_mathematical_expression()
    new_result = (calculate_mathematical_expression(num1, num2, operator2))
    return new_result


print(calculate_from_string('2 - 7'))