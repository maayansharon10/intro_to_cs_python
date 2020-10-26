import math


class Torpedo:

    """
    Torpedo object is part of Asteroids game.
    """

    def __init__(self, loc_x, loc_y, speed_x, speed_y, heading):
        """constructor of on object of type torpedo. radius and life points
        are constant.
        :param loc_x
        :param loc_y
        :param speed_x
        :param speed_y
        :param heading"""
        self.__loc_x = loc_x
        self.__loc_y = loc_y
        self.__speed_x = speed_x
        self.__speed_y = speed_y
        self.__heading = heading
        self.__radius = 4
        self.__life_points = 200

    def get_heading(self):
        """ :return heading (int representing degrees"""
        return self.__heading

    def has_intersection(self, obj):
        """
        Check if torpedo has collided with another object.
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

    def get_loc_x(self):
        """:return current location on x axis (float) of torpedo"""
        return self.__loc_x

    def get_speed_x(self):
        """:return current speed on x axis (float) of torpedo"""
        return self.__speed_x

    def get_loc_y(self):
        """:return current location on y axis (float) of torpedo"""
        return self.__loc_y

    def get_speed_y(self):
        """:return current speed on y axis (float) of torpedo"""
        return self.__speed_y

    def change_location(self, new_loc_x, new_loc_y):
        """
        set new values for location in axis x,y
        :param new_loc_x: location of torpedo in axis x (int)
        :param new_loc_y: location of torpedo in axis y (int)
        :return:
        """
        self.__loc_y = new_loc_y
        self.__loc_x = new_loc_x

    def change_speed(self, speed_x, speed_y):
        """
        set new values for speed x, speed y
        :param speed_x: speed of torpedo in axis x
        :param speed_y: speed of torpedo in axis y
        :return: None
        """
        self.__speed_x = speed_x
        self.__speed_y = speed_y

    def calculate_distance_to_object(self, obj):
        """
        Calculates the distance between torpedo and object,
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
        returns torpedo radius
        :return: torpedos radius (int or float)
        """

        return self.__radius

    def collision_condition(self, obj, distance):
        """
        Check if object is close enough to torpedo to clash.
        :param obj:
        :param distance:
        :return: True if clashes, else False
        """

        obj_radius = obj.get_radius()  # calculate other object radius

        return distance <= (self.__radius+obj_radius)  # True for clash,
        # else False
    
    def remove_torpedo_life(self, points_deducted):
        """
        update life points of torpedo
        :param points_deducted:
        :return:
        """
        self.__life_points -= points_deducted

    def get_life_points(self):
        """
        returns current torpedo life points
        :return: life_points (ints)
        """
        return self.__life_points
