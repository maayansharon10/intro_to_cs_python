import math


class Ship:
    
    """ Ship is an object intended to be a part of asteroids game"""
    
    def __init__(self, loc_x, loc_y):
        """constructor for an instance of type Ship. get location as param
        and has default values such as speed, heading, radius and life.
        :param loc_x
        :param loc_y"""
        self.__loc_x = loc_x
        self.__speed_x = 0
        self.__loc_y = loc_y
        self.__speed_y = 0
        self.__heading = 0
        self.__radius = 1
        self.__life = 3

    def remove_life(self):
        """
        remove 1 from amount of life ship has
        """
        self.__life -= 1
    
    def get_life_score(self):
        """ func returns a value of non negative int represent life score of
        ship"""
        return self.__life
    
    def set_life(self, new_life):
        """ recieves a non negative int as param and update as life points
        of ship. returns None """
        self.__life = new_life
        
    def get_loc_x(self):
        """:return current location on x axis (float) of ship"""
        return self.__loc_x
    
    def get_loc_y(self):
        """:return current location on y axis (float) of ship"""
        return self.__loc_y

    def get_speed_x(self):
        """:return current speed on x axis (float) of ship"""
        return self.__speed_x
    
    def set_speed_x(self, new_speed_x):
        """ :param new_speed_x (float)
        :return new speed location on x axis (float) of ship"""
        self.__speed_x = new_speed_x

    def get_speed_y(self):
        """:return current speed on y axis (float) of ship"""
        return self.__speed_y

    def set_speed_y(self, new_speed_y):
        """ :param new_speed_y (float)
        :return new speed location on y axis (float) of ship"""
        self.__speed_y = new_speed_y

    def get_heading(self):
        """:return current num of degrees represent heading (int) of ship"""
        return self.__heading
    
    def set_heading(self, new_heading):
        """ re - set heading as we wanted
        :param new_heading"""
        """:return update (int) of ship"""
        self.__heading = new_heading

    def change_heading(self, mode, degree):
        """ func change heading according to mode.
        :param mode ( l or r )
        mode 'l' (left) - add 7 degrees
        mode 'r' (right) - minus 7 degrees
        :param: degree (int)
        amount of change of original degree
        :return True upon success, False otherwise"""
        # change heading to the left
        if mode == 'l':
            self.__heading += degree

        # change heading to the right
        if mode == 'r':
            self.__heading -= degree

    def get_radius(self):
        """:return current radius (in int) of ship"""
        return self.__radius
    
    def change_location(self,  new_loc_x, new_loc_y,):
        """
        set new values for location in axis x,y
        :param new_loc_x: location of ship in axis x (int)
        :param new_loc_y: location of ship in axis y (int)
        :return: None
        """
        self.__loc_x = new_loc_x
        self.__loc_y = new_loc_y

    def change_speed(self, speed_x, speed_y):
        """
        set new values for speed x, speed y
        :param speed_x: speed of ship in axis x
        :param speed_y: speed of ship in axis y
        :return:
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
        ship_x = self.__loc_x
        ship_y = self.__loc_y

        return math.sqrt((obj_x-ship_x)**2+(obj_y-ship_y)**2)
    
  