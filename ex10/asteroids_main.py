from screen import Screen
import sys
import random
from ship import Ship
from asteroid import Asteroid
from torpedo import Torpedo
import math
DEFAULT_ASTEROIDS_NUM = 5
DEFAULT_CHANGE_DEGREE = 7
DEFAULT_ASTEROIDS_SIZE = 3
POINTS_DICT = {3: 20, 2: 50, 1: 100}  # in case of explosion, each size of
# exploding asteroid gets different number of points
MAX_TORPEDOS_IN_GAME = 10


class GameRunner:

    MSGS = {"collision": ("collision", "You collided with an astroid! -1 "
                                       "life"),
          "game_over_user": ("game_over", "you pressed q to exit game."
                             "goodbye, see you next time!"),
          "game_over_asteroids": ("game_over", "you destroyed all asteroids! "
                                               "Good job! You won!!"),
          "game_over_ship": ("game_over", "your ship ran out of life, "
                                          "You lost, Game Over buddy")}

    def __init__(self, asteroids_amount=5):
        """ a constructor of an instanse name of type GameRunner,
        it receives an amount of asteroids (with default value of 5 and
        contract a game. it creates shipm asteroids according to param and
        place them all on screen for game to start."""
        self.__screen = Screen()
        # Get default screen values from Screen class:
        self.__screen_max_x = Screen.SCREEN_MAX_X
        self.__screen_max_y = Screen.SCREEN_MAX_Y
        self.__screen_min_x = Screen.SCREEN_MIN_X
        self.__screen_min_y = Screen.SCREEN_MIN_Y

        # Calculate permanent values of difference between axises
        self.__delta_axis_x = self.__screen_max_x - self.__screen_min_x
        self.__delta_axis_y = self.__screen_max_y - self.__screen_min_y

        # Add other objects to the game
        self.__points = 0
        # Ship:
        self.__ship = self.create_ship()

        # Asteroids:
        self.__asteroids_amount = asteroids_amount
        self.__asteroid_list = []
        # Add all asteroids to the game and to the screen and add them to list:
        self.add_astroids_to_game(asteroids_amount)
        
        # Torpedos:
        self.__torpedos_list = []

    def get_points(self):
        """
        :return: points value
        """
        return self.__points

    def create_ship(self):
        """this func create an object of class Ship and draw it on screen
        :return : ship of class Ship"""

        # generate random locations for x and y
        loc_x, loc_y = self.get_random_location()
        
        # create an object of class Ship
        ship = Ship(loc_x, loc_y)

        return ship

    def random_ship_launch(self):
        """checks if user can choose to randomly place ship on screen by
        pressing't', if so update ship at new place"""

        speed_x = self.__ship.get_speed_x()
        speed_y = self.__ship.get_speed_y()
        heading = self.__ship.get_heading()
        life = self.__ship.get_life_score()

        if self.__screen.is_teleport_pressed():  # if user pressed 't'
            new_loc_x, new_loc_y = self.get_random_location()
            
            #  setting ship to be on new  loc
            self.__ship = Ship(new_loc_x, new_loc_y)
        
        # check ship and asteroid do not clash
            no_collisions = False
            
            while no_collisions is False:
                no_collisions = True
            
                for asteroid in self.__asteroid_list:
                    
                    while asteroid.has_intersection(self.__ship):
                        no_collisions = False
                        new_loc_x, new_loc_y = self.get_random_location()
                        self.__ship = Ship(new_loc_x, new_loc_y)
                        
            # setting new ship attributes to be the same as last ship
            self.__ship.set_speed_x(speed_x)
            self.__ship.set_speed_y(speed_y)
            self.__ship.set_heading(heading)
            self.__ship.set_life(life)
            
    def get_random_location(self):
        """
        returns random values for location coordinates, in boundaries of
        screen size
        :return: (coordinate, coordinate) tuple of ints
        """
        loc_x = random.randint(self.__screen_min_x, self.__screen_max_x)
        loc_y = random.randint(self.__screen_min_y, self.__screen_max_y)
        return loc_x, loc_y
    
    def msg_to_user(self, mode):
        """display msg to user on screen according to mode.
        mode 1 - game over - asteroids were distroyed
        mode 2 - game over - ship has no life
        mode 3 - game over - user exit
        mode 4 - collision had happend"""
        if mode == 1:
            self.__screen.show_message(self.MSGS["game_over_asteroids"][0],
                                       self.MSGS["game_over_asteroids"][1])
        elif mode == 2:
            # ship ran out of life
            self.__screen.show_message(self.MSGS["game_over_ship"][0],
                                       self.MSGS["game_over_ship"][1])
        elif mode == 3:
            # user pressed q to exit game
            self.__screen.show_message(self.MSGS["game_over_user"][0],
                                       self.MSGS["game_over_user"][1])
        elif mode == 4:
            self.__screen.show_message(self.MSGS["collision"][0],
                                       self.MSGS["collision"][1])
        else:
            return None
        
    def _is_game_over(self):
        """ check if game is over. if so, prints an informative msg
        to user and returns True, else - returns false
        :return True if game is over, False - otherwise"""

        # check ship has no life point
        if self.__ship.get_life_score() == 0:
            self.msg_to_user(2)  # msg ship ran out of life
            return True
    
        # check all asteroids exploded
        elif not self.__asteroid_list:  # if list is empty
            self.msg_to_user(1)  # game over because asteroids destroyed
            return True
        
        # user pressed 'q' to exit game
        elif self.__screen.should_end():
            self.msg_to_user(3)  # msg user decided to exit game
            return True
        
        else:  # game is not over
            return False

    def run(self):
        """ run game  (with do_loops() ) and activate screen"""
        self._do_loop()
        self.__screen.start_screen()

    def _do_loop(self):
        """run one game loop"""
        # You don't need to change this method!
        self._game_loop()

        # Set the timer to go off again
        self.__screen.update()
        self.__screen.ontimer(self._do_loop, 5)

    def _game_loop(self):
        """this func do one loop of the game. it checks if changes happen
        in any object of the game according to user's moves or if collisions
        or explosions happennd and update all objects and screen
        accordingly. in case game is over - it exit game """
        # ship:
        self.__screen.draw_ship(self.__ship.get_loc_x(),
                                self.__ship.get_loc_y(),
                                self.__ship.get_heading())  # draw on screen

        self.move_object(self.__ship)                      # change location
        self.change_ship_heading()                         # change heading
        self.change_object_speed(self.__ship)              # change speed

        # Launch a torpedo:
        self.launch_a_torpedo()

        # Check collisions (Asteroid and ship)
        self.collision()  # check for collisions, remove life and show msg
        
        # Check explosions (Torpedos and Asteroids)
        self.explosions()  # check for collisions, remove life, erase torpedo
        # and show msg

        # Move objects on screen:
        self.move_all_objects("Torpedo", self.__torpedos_list)
        self.move_all_objects("Asteroid", self.__asteroid_list)
        
        # Update all torpedos' status - check life points and if bellow 0 -
        # erase from torpedo_list.
        self.update_torpedo_status(self.__torpedos_list)
        
        # check if user pressed 't' to randomly place ship on screen
        self.random_ship_launch()  # check ship does not collide with
        # asteroids
        
        # Check if game should end
        result = self._is_game_over()  # returns a bool

        if result:  # if game is over
            self.__screen.end_game()
            sys.exit()
        
    ### collision functions ###

    def explosions(self):
        """
        Main function for handling explosions in game.
        1) looks for collisions of torpedos and asteroids.
        2) If a collision has been detected:
            a) raise points of game, show to user
            b) change size of asteroid or make it disappear
            c) erase torpedo from game
        """

        # Check all combinations of asteroids and torpedos
        for asteroid in self.__asteroid_list:
            for torpedo in self.__torpedos_list:

                if asteroid.has_intersection(torpedo):  # Explosion detected
                    self.raise_points(asteroid)  # add points
                    self.asteroid_reaction_to_explosion(asteroid, torpedo)
                    self. update_torpedo_status(self.__torpedos_list, 2,
                                                torpedo)
    
    def calc_new_speed_after_explosion(self, torpedo_speed, curr_speed_x,
                                       curr_speed_y, axis):
        """
        Calculate new asteroid speed, as influenced by the hit torpedo and 
        original asteroid.
        
        :param torpedo_speed: float 
        :param curr_speed_x:  int
        :param curr_speed_y:  int
        :param axis:  "X" or "Y"
        :return: new speed (float)
        """

        # Next lines are according to given formula:
        if axis == "X":
            numerator = torpedo_speed + curr_speed_x
        else:  # axis == "Y":
            numerator = torpedo_speed + curr_speed_y

        denominator = math.sqrt(curr_speed_x ** 2 + curr_speed_y ** 2)

        new_speed = numerator/denominator
        return new_speed

    def get_new_speed_in_all_axis(self, torpedo, org_asteroid):
        """ calc new speed for asteroid after hitting a torpedo.
        :param torpedo object, asteroid object.
        :return new_speed_x, new_speed_y (int)"""
        torpedo_speed_x = torpedo.get_speed_x()
        torpedo_speed_y = torpedo.get_speed_y()

        curr_speed_x = org_asteroid.get_speed_x()
        curr_speed_y = org_asteroid.get_speed_y()

        new_speed_x = self.calc_new_speed_after_explosion(torpedo_speed_x,
                                                          curr_speed_x,
                                                          curr_speed_y, "X")
        new_speed_y = self.calc_new_speed_after_explosion(torpedo_speed_y,
                                                          curr_speed_x,
                                                          curr_speed_y, "Y")

        return new_speed_x, new_speed_y
 
    def asteroid_reaction_to_explosion(self, org_asteroid, torpedo):
        """after asteroid ecploded - it changes it size. if its size is one
        - remove from game
        :param org_asteroid (asteroid object), torpedo object"""
        asteroid_size = org_asteroid.get_size()

        if asteroid_size == 1:
            self.remove_astroid_from_game(org_asteroid)  # remove old asteroid

        elif asteroid_size > 1:
            new_size = asteroid_size-1

            # calculate new asteroids speed values, one opposite to the other

            new_speed1_x, new_speed1_y = self.get_new_speed_in_all_axis(
                                        torpedo, org_asteroid)
            new_speed2_x, new_speed2_y = (-1)*new_speed1_x, (-1)*new_speed1_y

            self.create_single_asteroid(new_size, org_asteroid.get_loc_x(),
                                        org_asteroid.get_loc_y(),
                                        new_speed1_x, new_speed1_y)
            self.create_single_asteroid(new_size, org_asteroid.get_loc_x(),
                                        org_asteroid.get_loc_y(),
                                        new_speed2_x, new_speed2_y)

            self.remove_astroid_from_game(org_asteroid)  # remove old asteroid

    def raise_points(self, asteroid):
        """
        In case a tropedo hit an asteroid, game points will be raised. This
        function adds points to the game, and show new value on screen.
        :param asteroid: instance of class asteroid.
        """

        asteroid_size = asteroid.get_size()  # points depend on asteroid size
        points_to_raise = POINTS_DICT[asteroid_size]  # get value of asteroid
        self.__points += points_to_raise             # add points
        self.__screen.set_score(self.get_points())  # Show on screen

    def collision(self):
        """
        Main function for handling collisions in game.
        1) looks for collisions of asteroids.
        2) If a collision has been detected, shows a msg to user, decrease
        life from ship, remove asteroid from screen and from list of asteroids.
        """

        collided_asteroid = self.collision_detector()

        if collided_asteroid:
            self.msg_to_user(4)
            self.__screen.remove_life()
            self.__ship.remove_life()
            self.remove_astroid_from_game(collided_asteroid)

    def collision_detector(self):
        """
        Go over all asteroids, check if collision has been detected.
        :return: If a collision has been detected, return pointer to
        collided asteroid. Else, return None.
        """
        for asteroid in self.__asteroid_list:

            if asteroid.has_intersection(self.__ship):
                return asteroid

        return None

    def remove_astroid_from_game(self, collided_asteroid):
        """
        remove the given asteroid from list of asteroids in this game.
        remove the given asteroid from screen.
        :param collided_asteroid: instance of class Asteroid
        """

        if collided_asteroid in self.__asteroid_list:
            self.__asteroid_list.remove(collided_asteroid)
            self.__screen.unregister_asteroid(collided_asteroid)


    ### Basic Movement Functions ###

    def change_ship_heading(self):

        """
        According to user presses on right/left arrows-keys, turn ship's degree
        """

        if self.__screen.is_left_pressed():  # if user pressed left
            self.__ship.change_heading('l', DEFAULT_CHANGE_DEGREE)  # update
            # heading to left

        elif self.__screen.is_right_pressed():  # if user pressed right
            self.__ship.change_heading('r', DEFAULT_CHANGE_DEGREE)

    def move_all_objects(self, object_class, list_of_objects):

        """
        Change all objects locations and update on screen
        """

        for obj in list_of_objects:  # go over all objects in game

            # change location:
            self.move_object(obj)
            # draw on screen:
            if object_class == "Torpedo":
                self.__screen.draw_torpedo(obj, obj.get_loc_x(),
                                           obj.get_loc_y(),
                                           obj.get_heading())
            elif object_class == "Asteroid":
                self.__screen.draw_asteroid(obj, obj.get_loc_x(),
                                            obj.get_loc_y())

    def move_object(self, obj):
        """
        Gets an object of class Ship or Astroid,
        calculates it's new coordinates
        and change location in the object instance.
        :param obj: object of class Ship, Astroid
        """
        
        new_y = self.calc_new_location(obj.get_speed_y(),
                                       obj.get_loc_y(),
                                       self.__delta_axis_y,
                                       self.__screen_min_y)
        new_x = self.calc_new_location(obj.get_speed_x(),
                                       obj.get_loc_x(),
                                       self.__delta_axis_x,
                                       self.__screen_min_x)
        obj.change_location(new_x, new_y)

    def calc_new_location(self, speed, old_coord, delta_axis, axis_min_coord):
        """
        This function gets various parameters, all refer to same axis.
        It sets the new location of an object in asteroids game,  on that axis.
        The calculation is according to a given formula.

        :param speed: float
        :param old_coord: old coordinate on this axis (int)
        :param delta_axis: The permanent value of :Axis Max coordinate - Axis
        Min coordinate (int)
        :param axis_min_coord: The min coordinate in this axis
        :return: New coordinate (int)
        """

        first_part = (speed + old_coord - axis_min_coord)
        new_coord = (first_part % delta_axis + axis_min_coord)

        return new_coord

    def change_object_speed(self, obj):
        """
        Gets an object of class Ship or Astroid,
        calculates it's new speed
        and change speed in the object instance.
        :param obj: object of class Ship, Astroid
        """
        if self.__screen.is_up_pressed():  # User pressed up arrow key
            new_speed_y = self.calc_new_speed("Y", obj.get_speed_y(),
                                                  obj.get_heading())
            new_speed_x = self.calc_new_speed("X", obj.get_speed_x(),
                                              obj.get_heading())
            obj.change_speed(new_speed_x, new_speed_y)

    def calc_new_speed(self, axis, curr_speed, curr_heading):

        """
        Calculates the acceleration of an object.
        :param axis: "X" or "Y", determines which trigonometric func to use
        :param curr_speed:  speed in curr axis (float)
        :param curr_heading: location in curr axis (float)
        :return: new_speed (float)

        """
        # This formula uses radians. since heading is in degrees - convert:
        curr_heading_in_radians = math.radians(curr_heading)

        # calculate second part of the formula - use cos() for x, sin() for y:
        second_part_of_formula = math.cos(curr_heading_in_radians) if \
            axis == "X" else math.sin(curr_heading_in_radians)

        new_speed = curr_speed + second_part_of_formula

        return new_speed

    ### asteroids functions ###
    def create_single_asteroid(self, size, loc_x, loc_y, speed_x, speed_y):
        """
        Creates a single iteration of an asteroid:
        * sets first values as given as inputs
        * fix locations if a collision has been found
        * add new asteroid to screen
        * add new asteroid to the list of asteroids-pointers
        :param size:
        :param loc_x:
        :param loc_y:
        :param speed_x:
        :param speed_y:
        """
        # create an object of class Astroid
        asteroid = Asteroid(size, loc_x, loc_y, speed_x, speed_y)

        # avoid adding ship in coordinate of intersection with ship
        while asteroid.has_intersection(self.__ship):
            loc_x, loc_y = self.get_random_location()
            asteroid.change_location = (loc_x, loc_y)

        # add to list of asteroids
        self.__asteroid_list.append(asteroid)

        # register to screen
        self.__screen.register_asteroid(asteroid, size)

    def add_astroids_to_game(self, num):
        """
        Handles process of adding asteroids to the game.
        Creates num instances of class Asteroid, for each one:
        * sets first values
        * fix locations if a collision has been found
        * add new asteroid to screen
        * add new asteroid to the list of asteroids-pointers
        """

        asteroid_list = []

        for i in range(num):
            # create the i astroid, and add it to list:

            # generate random locations for x and y
            loc_x, loc_y = self.get_random_location()

            # generate random speed for x and y
            init_speed_x = random.randint(1, 4)
            init_speed_y = random.randint(1, 4)

            self.create_single_asteroid(DEFAULT_ASTEROIDS_SIZE, loc_x, loc_y,
                                        init_speed_x, init_speed_y)

    ### Torpedo functions ###

    def create_new_torpedo(self):
        """
        Create a new Torpedo instance and calculates all its values
        :return: Torpedo class instance
        """
        # x,y are the same as ship at time of shooting
        loc_x, loc_y = self.__ship.get_loc_x(), self.__ship.get_loc_y()

        # generate speed values
        init_speed_x, init_speed_y = self.calc_torpedo_speed("x"), \
                                     self.calc_torpedo_speed("y")

        heading = self.__ship.get_heading()
        # create a new Torpedo instance
        new_torpedo = Torpedo(loc_x, loc_y, init_speed_x, init_speed_y,
                              heading)

        return new_torpedo

    def calc_torpedo_speed(self, axis):
        """
        Calculates torpedo speed according to this formula:
        for axis x:
        newspeed = currentspeed + 2*cos(CurrentHeadingInRadians)
        for axis y:
        newspeed = currentspeed + 2*sin(CurrentHeadingInRadians)

        Note: all initial values are set by current ship values, which the
        torpedo has been shot from

        :param axis: "x" or "y"
        :return:
        """
        # This formula uses radians. since heading is in degrees - convert:
        curr_heading_in_radians = math.radians(self.__ship.get_heading())
        
        if axis == "x":
            ship_speed_at_launch = self.__ship.get_speed_x()
            second_part = 2*math.cos(curr_heading_in_radians)

        else:  # axis == "y":
            ship_speed_at_launch = self.__ship.get_speed_y()
            second_part = 2 * math.sin(curr_heading_in_radians)

        newspeed = ship_speed_at_launch + second_part

        return newspeed


    def launch_a_torpedo(self):
        """Handles process of adding a torpedo to the game:
        if torpedo can be added to game -
        * Creates an instance of class Torpedo, sets first values
        * Add torpedo to list of torpedos
        * add new torpedo to screen
        """
        num_of_torpedos_in_game = len(self.__torpedos_list)

        if self.__screen.is_space_pressed():
            # create the torpedo instance:
            if num_of_torpedos_in_game < MAX_TORPEDOS_IN_GAME:
                # Only if there's less then max torpedos in game
                
                torpedo = self.create_new_torpedo()
        
                # add to list of torpedos in game:
                self.__torpedos_list.append(torpedo)
        
                # register to screen
                self.__screen.register_torpedo(torpedo)

    def remove_torpedo_from_game(self, torpedo):
        """:param torpedo object
        takes torpedo off torpedo list and also remove from screen"""
        if torpedo in self.__torpedos_list:
            self.__torpedos_list.remove(torpedo)
            self.__screen.unregister_torpedo(torpedo)

    def update_torpedo_status(self, torpedos_list, mode=1,
            torpedo_to_remove=None):
        """
        mode 1 -
        update all topedos life points and if goes bellow 0 - erase from game
        mode 2 -
        collision happened, erase torpedo form game
        :param torpedos_list, mode (default = 1, else - 2),
        torpedo_to_remove (default - None)
        :return:
        """
        if mode == 1:
            for torpedo in torpedos_list:  # for each torpedo in game
            
                life_points = torpedo.get_life_points()  # int from 0 to 200
            
                if life_points <= 0:  # torpedo has no life
                    # points - erase it
                    self.remove_torpedo_from_game(torpedo)
            
                else:  # life_points > 0 torpedo still has life points
                    torpedo.remove_torpedo_life(1)  # -1 life point
                    
        if mode == 2:  # collision happened, erase torpedo
            if torpedo_to_remove in torpedos_list:
                self.remove_torpedo_from_game(torpedo_to_remove)


def main(amount):
    """func create a game instance of type GameRunner and then runs it with
    run method"""
    runner = GameRunner(amount)
    runner.run()


if __name__ == "__main__":
    if len(sys.argv) > 1:  # we must receive at lease one argument from
        # command line
        main(int(sys.argv[1]))
    else:
        main(DEFAULT_ASTEROIDS_NUM)
