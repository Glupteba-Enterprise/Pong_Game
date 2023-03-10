"""pong gmaing"""
# TODO: BALL PHYSICS/VECTORS
import tkinter as tk
from tkinter import *
import time

# defining variables
gui_title = "Glupteba Pong"
gui_text = "The Big Glup"
gui_width = 500
gui_height = 500
game_states = ['MENU', 'GAMING']
game_state = game_states[0]
# creating gui instance
gui_main = tk.Tk()

"""getting the screen center"""

# getting screen dimensions
screen_width = gui_main.winfo_screenwidth()
screen_height = gui_main.winfo_screenheight()
# calculating the screen center
gui_x = int(screen_width / 2 - gui_width / 2)
gui_y = int(screen_height / 2 - gui_height / 2)


def onKeyPress(event):
    """Moves paddles when keys pressed.

    Arguments:
    event: Given by .bind (do not enter yourself), the key that has been pressed.
    Returns:
    Nope :P

    In our canvas, (0, 0) is the top left, (1, 1) is the bottom right.
    WS moves left paddle, up/down keys moves right padde (up/down movement only)
    Also removes introduction label.
    """

    start_game()
    # find current position of paddles
    ypos_paddle1 = get_relative_coordinates(paddle_1, "y")
    ypos_paddle2 = get_relative_coordinates(paddle_2, "y")

    # moves paddles
    if event.keysym == 'w':  # left paddle up
        if ypos_paddle1 > 0.075:
            paddle_1.place(relx=0, rely=ypos_paddle1 - 0.025, anchor=CENTER)
    elif event.keysym == 's':  # left paddle down
        if ypos_paddle1 < 0.925:
            paddle_1.place(relx=0, rely=ypos_paddle1 + 0.025, anchor=CENTER)
    # (right paddle is fixed)
    if event.keysym == 'Up':  # right paddle up
        if ypos_paddle2 > 0.075:
            paddle_2.place(relx=1, rely=ypos_paddle2 - 0.025, anchor=CENTER)
    if event.keysym == 'Down':  # right paddle down
        if ypos_paddle2 < 0.925:
            paddle_2.place(relx=1, rely=ypos_paddle2 + 0.025, anchor=CENTER)


def get_relative_coordinates(canvas, coordinate):
    """Returns relative y or x value of canvas.

      Arguments:
      canvas: The canvas whose coordinate is being checked. Generally the paddles.
      coordinate: x or y, the coordinate being checked. Raises an exception if this is not a valid coordinate.

      Returns:
      The relative y or value of the canvas (none of the useless stuff the function place_info() has) (a float)
    """
    if coordinate == "x":
        return float(canvas.place_info()["relx"])
    elif coordinate == "y":
        return float(canvas.place_info()["rely"])
    else:
        raise Exception("There are only x and y coordinates: input 'x' or 'y' to function get_relative_coordinates")

def start_game():
    """Starts the game processes"""
    # change game state
    global game_state
    game_state = game_states[1]
    # destroy menu variable
    gui_label.destroy()
    # add game variable
    middle_line = tk.Canvas(gui_main, bg='white', height=400, width=10)
    middle_line.place(relx=0.5, rely=0.5, anchor=CENTER)

# setting gui variables
gui_main.title(gui_title)
gui_canvas = Canvas(gui_main)
gui_canvas.create_rectangle(400, 400, 1, 1, fill='black')
gui_canvas.pack()
gui_label = tk.Label(gui_main, text='Glup Any Key To Start!', bg='black', fg='green')
gui_label.place(relx=0.5, rely=0.5, anchor='center')

paddle_1 = tk.Canvas(gui_main, bg='white', height=100, width=10)
paddle_1.place(relx=0, rely=0.5, anchor=CENTER)

paddle_2 = tk.Canvas(gui_main, bg='white', height=100, width=10)
paddle_2.place(relx=1, rely=0.5, anchor=CENTER)

ball = gui_canvas.create_rectangle(10, 10, 50, 50, fill='white')
# listens for any 'KeyPress' event
gui_main.bind('<KeyPress>', onKeyPress)

# run the gui
gui_main.mainloop()
