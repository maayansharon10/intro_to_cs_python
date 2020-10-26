#importing math - required when using math module.
import math

def golden_ratio():
    """function which prints out Goldan Rathio """
    print (float ( (1+ (5**0.5)) / 2 ))


def six_cubed():
    """function which prints the number 6 powered by 3."""
    print (math.pow(6, 3))



def hypotenuse():
    """function which prints out the the hypotenuse of a right triangle when
    its ribs are 3 and 5, using the Pythagorean equation"""
    x = ( ( math.pow(3, 2)) + (math.pow(5, 2)) )
    print ( math.pow(x, 0.5) )

def pi():
    """a function which prints out the value of the number pi"""
    print (math.pi)

def e():
    """a function which prints out the value of the number e"""
    print (math.e)

def triangular_area():
    """a function which prints out the area of right and isosceles triangles
    when their ribs are 1 to 10 """
    print( ((math.pow(1,2))/2), (math.pow(2,2)/2), (math.pow(3,2)/2),
        (math.pow(4,2)/2), (math.pow(5,2)/2),  (math.pow(6,2)/2),
        (math.pow(7,2)/2), (math.pow(8,2)/2),  (math.pow(9,2)/2),
        (math.pow(10,2)/2) )


if __name__ == "__main__" :
    golden_ratio()
    six_cubed()
    hypotenuse()
    pi()
    e()
    triangular_area()
