class Car:
    """
    build objects from type car with name, len, location, orientation and
    operates methosed on them
    """
    VERTICAL = 0
    HORIZONTAL = 1
    
    def __init__(self, name, length, location, orientation):
        """
        A constructor for a Car object
        :param name: A string representing the car's name
        :param length: A positive int representing the car's length.
        :param location: A tuple representing the car's head (row, col)location
        :param orientation: One of either 0 (VERTICAL) or 1 (HORIZONTAL)
        """
        # Note that this function is required in your Car implementation.
        # However, is not part of the API for general car types.
        self.__name = name
        self.__length = length
        self.__location = location
        self.__orientation = orientation

    def __get_location(self):
        return self.__location

    def __get_length(self):
        return self.__length
    
    def __get_orientation(self):
        return self.__orientation
    
    def car_coordinates(self):
        """
        :return: A list of coordinates the car is in
        """
        coordination_lst = []
        car_head = self.__location
        row, col = car_head
        car_length = self.__length
        car_orientation = self.__orientation
        if car_orientation == self.VERTICAL:  # orientation is vertical
            for coordination in range(car_length):
                coordination_lst.append((row, col))
                row = row + 1
        if car_orientation == self.HORIZONTAL:  # orientation is horizontal
            for coordination in range(car_length):
                coordination_lst.append((row, col))
                col = col + 1
        return coordination_lst

    def possible_moves(self):
        """
        :return: A dictionary of strings describing possible movements permitted by this car.
        """
        # For this car type, keys are from 'udrl'
        # The keys for vertical cars are 'u' and 'd'.
        # The keys for horizontal cars are 'l' and 'r'.
        # You may choose appropriate strings.
        # implement your code and erase the "pass"
        # The dictionary returned should look something like this:
        # result = {'f': "cause the car to fly and reach the Moon",
        #          'd': "cause the car to dig and reach the core of Earth",
        #          'a': "another unknown action"}
        # A car returning this dictionary supports the commands 'f','d','a'.
        orientation = self.__orientation
        if orientation == self.VERTICAL:  # if car orientation is vertical
            possible_moves_dict = {"u": "cause the car to go up one move ",
                                   "d": "cause the car to go down one move"}
        else:  # if orientation == Car.HORIZONTAL
            possible_moves_dict = {"r": "cause the car to go right one move ",
                                   "l": "cause the car to go left one move"}
        return possible_moves_dict
        
    def movement_requirements(self, movekey):
        """
        :param movekey: A string representing the key of the required move.
        :return: A list of cell locations which must be empty in order for this move to be legal.
        """
        
        # ??? can we assume the movekey would be valid???????????????????
        # For example, a car in locations [(1,2),(2,2)] requires [(3,2)] to
        # be empty in order to move down (with a key 'd').
        # implement your code and erase the "pass"
        car_length = self.__length
        car_places = self.car_coordinates()  # list of coordinates car is in
        row, col = self.__location
        
        # for each possible movekey - create a new_empty_cell that should be
        #  empty
        req_list = []   # list with required empty list for move from
                        # type 'movekey'
        if movekey == 'u':
            new_empty_cell = (row - 1, col)
            req_list.append(new_empty_cell)
        elif movekey == 'd':
            row = car_places[car_length - 1][0] + 1  # take the last
            # coordinate of the car(it's 'tail') + 1
            new_empty_cell = (row, col)
            req_list.append(new_empty_cell)
        elif movekey == 'l':
            new_empty_cell = (row, col - 1)
            req_list.append(new_empty_cell)
        elif movekey == 'r':
            col = car_places[car_length - 1][1] + 1  # take the last
            # coordinate of the car (it's tail) + 1
            new_empty_cell = (row, col)
            req_list.append(new_empty_cell)
            
        return req_list
        
    def move(self, movekey):
        """
        :param movekey: A string representing the key of the required move.
        :return: True upon success, False otherwise
        """
        # try to move the location of the car
        row, col = self.__location  # unpack tuple
        if movekey in self.possible_moves():  # if it is a valid movekey
            if movekey == 'u':
                row = row - 1
                
                self.__location = (row, col)
            elif movekey == 'd':
                row = row + 1
                self.__location = (row, col)
            elif movekey == 'l':
                col = col - 1
                self.__location = (row, col)
            else:  # movekey == 'r':
                col = col + 1
                self.__location = (row, col)
            return True
        return False  # if move was not valid
        
    def get_name(self):
        """
        :return: The name of this car.
        """
        return self.__name
