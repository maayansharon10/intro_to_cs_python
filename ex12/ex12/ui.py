import tkinter as tk
from .game_runner import *
from .game import *


class UI:
    """Gui for playing Four in a Row, applicable to Controller class."""

    def __init__(self, controller):

        self.controller = controller
        self.root = tk.Tk()
        self.emptycell = tk.PhotoImage(file="ex12/freecell.png")
        self.bluecell = tk.PhotoImage(file="ex12/blue_cell.png")
        self.redcell = tk.PhotoImage(file="ex12/red_cell.png")
        self.cvcimg = tk.PhotoImage(file="ex12/cvc.png")
        self.hvhimg = tk.PhotoImage(file="ex12/hvh.png")
        self.hvcimg = tk.PhotoImage(file="ex12/hvc.png")
        self.wonimg = tk.PhotoImage(file="ex12/won.png")
        self.gameovermachineimg = tk.PhotoImage(
            file="ex12/gameovermachine.png")
        self.gameoverhumanimg = tk.PhotoImage(file="ex12/gameoverhuman.png")
        self.gameovertieimg = tk.PhotoImage(file="ex12/gameovertie.png")
        self.startbg = tk.PhotoImage(file="ex12/startbg.png")
        self.wrongmoveimg = tk.PhotoImage(file="ex12/wrongmove.png")
        self.FIRST_PLAYER = 1
        self.SECOND_PLAYER = 2
        self.ROWS = 6
        self.COLS = 7
        self.height = 500
        self.width = 500
        self.top = tk.Toplevel()
        self.top.title("Welcome")
        self.top.resizable(width=False, height=False)
        self.top.geometry('790x540+300+0')
        self.big_frame = tk.Frame(self.root)  # main container
        self.big_frame.grid()
        self.start_frame = tk.Frame(self.top, bg="black")
        self.start_frame.grid()
        self.board_frame = tk.Frame(self.big_frame)  # frame for board
        self.board_frame.grid()
        self.on_start()  # Start screen (choosing players)

    def on_start(self):
        """building the start screen, which allows to create a new game and
        choose players."""

        lable_title = tk.Label(self.start_frame, text="Four In A Row:\n"
                                                      "Humanity against Robots"
                               , font=("Calibri", 20))
        lable_title.grid(row=2, column=1)
        hh_button = tk.Button(self.start_frame, image=self.hvhimg,
                              text="Human against a Human",
                              compound="top",
                              command=self._create_players_event(
                                  ["h", "h"]),
                              font=("Courier", 10))
        hh_button.grid(row=1, column=1)

        hm_button = tk.Button(self.start_frame, image=self.hvcimg,
                              text="Human against Robot",
                              compound="top",
                              command=self._create_players_event(
                                  ["h", "m"]),
                              font=("Courier", 10))
        hm_button.grid(row=2, column=0)
        hm_button = tk.Button(self.start_frame, image=self.hvcimg,
                              text="Robot against Human",
                              compound="top",
                              command=self._create_players_event(
                                  ["m", "h"]),
                              font=("Courier", 10))
        hm_button.grid(row=2, column=2)
        mm_button = tk.Button(self.start_frame, image=self.cvcimg,
                              text="Let the robots compete themselves",
                              compound="top",
                              command=self._create_players_event(
                                  ["m", "m"]),
                              font=("Courier", 10))
        mm_button.grid(row=3, column=1)

    def _create_players_event(self, type_list):
        """Creates the function for buttons in start screen"""

        def button_press():
            self.controller.add_players(type_list)  # Adds players to game
            self.top.destroy()  # closes current window
            self.root.lift()  # rises the board window
            self.draw_board()  # creates the board window

        return button_press

    def draw_board(self):
        """Creates the board screen, which includes buttons for each cell,
        which is updated by the current player who has this cell"""

        board = self.board_frame
        win_exit = self.controller.is_game_over()
        for row in range(self.ROWS):
            for col in range(self.COLS):
                # Find status of cell:

                if win_exit and \
                        [row, col] in self.controller.game.board.winning_set:
                    new_button = \
                        tk.Button(board, image=self.wonimg,
                                  command=self.controller.on_col_selected(
                                      col))
                    new_button.grid(row=row, column=col)
                    continue

                in_this_cell = self.controller.game.get_player_at(row, col)

                if in_this_cell is None:  # Empty cell case
                    new_button = tk.Button(board, image=self.emptycell,
                                           command=
                                           self.controller.on_col_selected(
                                               col))

                elif in_this_cell == self.FIRST_PLAYER:
                    new_button = tk.Button(board, image=self.bluecell,
                                           command=
                                           self.controller.on_col_selected(
                                               col))

                elif in_this_cell == self.SECOND_PLAYER:
                    new_button = tk.Button(board, image=self.redcell,
                                           command=
                                           self.controller.on_col_selected(
                                               col))

                new_button.grid(row=row, column=col)

    def game_over_screen(self, winner):
        """Creates the end-of-game screen, which offers a new game or exit"""

        gameoverscreen = tk.Toplevel()
        gameoverscreen.title("Game Over")
        gameoverscreen.resizable(width=False, height=False)

        if winner == 0:  # tie
            game_over_text = "No one won. (yet...)"

            img = self.gameovertieimg

        else:  # there's a winner
            game_over_text = "Victory was accomplished by player " + str(
                winner)
            if self.controller.get_current_player_type(winner) == "m":
                img = self.gameovermachineimg
                txt = "Be aware of the robots..."
            else:
                img = self.gameoverhumanimg
                txt = "Congratulations Humanity!"
            shortlable = tk.Label(gameoverscreen, text=txt,
                                  font=("Calibri", 15))
            shortlable.grid()

        # Main image and message in screen:

        pic = tk.Label(gameoverscreen, image=img)
        pic.grid()
        end_text = tk.Label(gameoverscreen, text=game_over_text,
                            font=("Calibri", 20))
        end_text.grid()

        # Buttons:
        start_again_button = tk.Button(gameoverscreen, text="New Game",
                                       command=self.click_start_new_game(),
                                       font=("Calibri", 20))
        start_again_button.grid()
        quit_button = tk.Button(gameoverscreen, text="Exit",
                                command=lambda: self.root.destroy(),
                                font=("Calibri", 20))
        quit_button.grid()

    def click_start_new_game(self):
        """function for clicking on new game"""

        def start_new_game():
            self.root.destroy()  # close window
            self.controller.reset_game()  # reset al variables and create a
            # new game instance
            self.controller.play()  # play again!

        return start_new_game

    def wrong_move_windows(self):
        """Display error to user"""

        new_window = tk.Toplevel(self.root)
        pic = tk.Label(new_window, image=self.wrongmoveimg)
        pic.grid()
        end_text = tk.Label(new_window, text="That's a wrong move!",
                            font=("Calibri", 20))
        end_text.grid()
        quit_button = tk.Button(new_window, text="OK",
                                command=lambda:
                                new_window.destroy(),
                                font=("Calibri", 20))
        quit_button.grid()
