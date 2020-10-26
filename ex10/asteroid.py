import math


class Asteroid:

    """
    Asteroid object is part of Asteroids game.
    """

    def __init__(self, size, loc_x, loc_y, speed_x, speed_y):
        """ constructor. construct an object of type Asteroid"""
        self.__loc_x = loc_x
        self.__loc_y = loc_y
        self.__speed_x = speed_x
        self.__speed_y = speed_y
        self.__size = size
        self.__radius = self.get_radius()

    def has_intersection(self, obj):
        """
        Check if asteroid has collided with another object.
        Uses 2 formulas, calculated in help functions:
        - Distance formula
        - collision-distance condition
        :param obj:
        :return: True if collision has been detected, else False
        """

        # calculate distance to the object
        distance = self.calculate_distance_to_object(obj)

        # return True if close enough to clash, else False:
        return self.collision_condition(obj, distance)

    def get_size(self):
        """ func return size (int)
        :return size"""
        return self.__size

    def get_loc_x(self):
        """func return location of axis x value (float)
        :return loc x"""
        return self.__loc_x

    def get_speed_x(self):
        """ returns the value of speed on axis x
        :return speed on axis x (float)"""
        return self.__speed_x

    def get_loc_y(self):
        """func return location of axis y value (float)
        :return loc y"""
        return self.__loc_y

    def get_speed_y(self):
        """ returns the value of speed on axis y
        :return speed on axis y (float)"""
        return self.__speed_y

    def change_location(self, new_loc_x, new_loc_y):
        """
        set new values for location in axis x,y
        :param new_loc_x: location of asteroid in axis x (int)
        :param new_loc_y: location of asteroid in axis y (int)
        :return: None
        """
        self.__loc_x = new_loc_x
        self.__loc_y = new_loc_y

    def change_speed(self, speed_x, speed_y):
        """
        set new values for speed x, speed y
        :param speed_x: speed of asteroid in axis x
        :param speed_y: speed of asteroid in axis y
        :return: None
        """
        self.__speed_x = speed_x
        self.__speed_y = speed_y

    def calculate_distance_to_object(self, obj):
        """
        Calculates the distance between asteroid and object,
        by the elementary distance formula:
        distance = sqrt((x1-x2)^2 +(y1-y2)^2)
        :param obj: instance of a class which has the attributes:
        coordinates in x axis, coordinates in y axis, and has methods of
        getting them get_loc_axis()
        :return: distance (float)
        """
        # Get values for formula - x,y coordinates:
        obj_x = obj.get_loc_x()
        obj_y = obj.get_loc_y()
        ast_x = self.__loc_x
        ast_y = self.__loc_y

        return math.sqrt((obj_x-ast_x)**2+(obj_y-ast_y)**2)

    def get_radius(self):
        """
        returns astroid radius
        :return: astroids radius (int or float)
        """

        return self.__size*10-5

    def collision_condition(self, obj, distance):
        """
        Check if object is close enough to asteroid to clash.
        :param obj:
        :param distance:
        :return: True if clashes, else False
        """

        obj_radius = obj.get_radius() # calculate other object radius

        return distance <= (self.__radius+obj_radius)   # True for clash,
                                                        # else False
