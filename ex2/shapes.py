""" זה אוטומטית חוזר לי לNONE לא משנה מה אני מקלידה"""

import math


def circle_area():
    """ receives input from user about the radius and calculates
    the area of a circle"""
    radius = float(input("choose radius"))

    circle_calc = radius*radius*math.pi
    return  circle_calc


def rectangle_area():
    """receives an input about 2 ribs and caculates the area of a circle"""
    edge_a = float(input())
    edge_b = float(input())
    calc_rectangle_area = edge_a*edge_b
    return calc_rectangle_area


def triangle_area():
    """all 3 ribs are the same. recives an input about a rib and caculates
    the area of a circle"""
    t_edge = float(input("insert triangle edge"))
    clac_triangle = (((3**0.5)/4) * (t_edge**2))
    return clac_triangle


def shape_area():
    """this function will recieve an input from user regarging the shape,
    circle, traingle or ractangle, then it will aske the user for mesures
    and caculate the area of the shape. it reutrns the size of the area"""
    user_shape = int(input("Choose shape (1=circle, 2=rectangle, "
                          "3=triangle): "))
    if user_shape == 1:
        # will call circle_area and return it's value
        return circle_area()
    elif user_shape == 2:
        # will  call rectangle_area and return it's value
        return rectangle_area()
    elif user_shape == 3:
        # will  call triangle_area and return it's value
        return triangle_area()
    else:
        return None