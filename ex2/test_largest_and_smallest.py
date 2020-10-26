import math
from largest_and_smallest import largest_and_smallest


def testing_s_and_l_func():
    """extreme cases -
    we will examine extreme cases in order to check if
    if function runs well even under those circumstances"""
    func_works = True
    case_1 = largest_and_smallest(0, 0, 0)
    # if all numbers are the same
    if case_1[0] == 0 and case_1[1] == 0:
        func_works = True
    else:
        func_works = False

    case_2 = largest_and_smallest(1, 3, 5)
    # if all numbers are not the same
    if case_2[0] == 5 and case_2[1] == 1:
        func_works = True
    else:
        func_works = False

    case_3 = largest_and_smallest(0, 0, 5)
    # if num1=mun2 and num3 is the largest
    if case_3[0] == 5 and case_3[1] == 0:
        func_works = True
    else:
        func_works = False

    case_4 = largest_and_smallest(5, 5, 1)
    # if num1=num2 and num 3 is the smallest
    if case_4[0] == 5 and case_4[1] == 1:
        func_works = True
    else:
        func_works = False
    # delete the print later!

    case_5 = largest_and_smallest(5, 3, 3)
    # if num2=num3 and num 1 is the largest
    if case_5[0] == 5 and case_5[1] == 3:
        func_works = True
    else:
        func_works = False
    return func_works


def test_results():
    if testing_s_and_l_func():
        print("Function 4 test success")
    else:
        print("function 4 test failed")
    return


if __name__ == '__main__':
    test_results()