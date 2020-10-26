import math

def quadratic_equation(a, b, c):
    """this function solves the quadratic equation while
    receiving 3 unknown numbers a,b,c and returns 2 known numbers """
    delta = ( b*b - 4*a*c )
    # to any quadric ecuation there are 3 options of solutions-
    # one when delta>0, =0, <0. we will check all of them in order
    # to get a precise solution.
    if delta > 0:
        # first case, leads to 2 different solution (x1,x2)
        x1 = (-b + math.sqrt(delta))/(2*a)
        x2 = (-b - math.sqrt(delta))/(2*a)
    elif delta < 0:
        # second case, leads to no solution to the equation
        x1=None
        x2=None
    else:
        # third case, when delta ==0, then there is only 1 solution (x1)
        x1 = (-b + math.sqrt(delta))/(2*a)
        x2 = None
    return x1, x2


def quadratic_equation_user_input():
    """this function gets 3 coefficients from user, puts them in
    quadratic_equation and prints out the solutions"""
    user_input = (input('Insert coefficients a, b, and c: '))
    a, b, c = user_input.split(" ")
    # split into a,b,c in order to put them in quadratic_equation
    q1, q2 = quadratic_equation(float(a), float(b), float(c))
    # new names for x1, x2 for user's choice for coefficients
    # there are 3 cases, we will address all 3 of them:
    if (q1 is None) and (q2 is None):
        # delta<0 - no solution
        print("The equation has no solutions")
    elif q2 is None:
        # delta ==0, there is only one solutioquadratic_equation_user_input():n
        print("The equation has 1 solution: " + str(q1))
    else:
        # delta>0, there are 2 different solutions
        print("The equation has 2 solutions: "+ str(q1) + " and "
              + str(q2))
    return

