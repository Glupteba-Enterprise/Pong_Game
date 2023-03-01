"""pong gmaing"""
import tkinter as tk
from tkinter import *

# defining variables
gui_title = "Glupteba Pong"
gui_text = "The Big Glup"
gui_width = 500
gui_height = 500

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
    """Our function that we later call in the KeyPress event listener.

    Note that when calling this function, filling in the 'event' field is not necessary. We should only be calling this
    function once in the 'bind()' gui function regardless.
    In our canvas, '0, 0' is the top left coordinates, '1, 1' is the bottom right coordinates.
    """

    # destroy the "press any key to start" label
    gui_label.destroy()

    ypos_paddle1 = float(split_place_info(paddle_1))
    ypos_paddle2 = float(split_place_info(paddle_2))
    # handle paddle movements
    if event.char == 'w':
        if ypos_paddle1 > 0.075:
            paddle_1.place(relx=0, rely=ypos_paddle1 - 0.025, anchor=CENTER)
    elif event.char == 's':
        if ypos_paddle1 < 0.925:
            paddle_1.place(relx=0, rely=ypos_paddle1 + 0.025, anchor=CENTER)
    # idk what the arrow keys are, tried 'up' and 'down'
    if event.char == '??':
        if ypos_paddle2 > 0.075:
            paddle_2.place(relx=0, rely=ypos_paddle2 - 0.025, anchor=CENTER)
    if event.char == '??':
        if ypos_paddle2 < 0.925:
            paddle_2.place(relx=0, rely=ypos_paddle2 + 0.025, anchor=CENTER)
def split_place_info(canvas):
    """Returns the canvas rely

    The place_info func returns a long string of unneeded info.
    We split this string on ',' and then get the fourth index in the new list.
    This returns "'rely': '0.5'", with 0.5 being the actual rely number.
    We then iterate through this string to create a new string comprising of only digits and decimal points.

    There is probably a better way to do this, especially the last part, dont glup me on this one ok.
    """
    return_string = ''
    for i in canvas.place_info().__str__().split(',')[4]:
        if i.isdigit() == True or i.__eq__('.'):
            return_string += i
    return return_string

# setting gui variables
gui_main.title(gui_title)
gui_main.geometry(f'{gui_width}x{gui_height}+{gui_x}+{gui_y}')  # width x height ± x ± y
gui_main.configure(bg='black')
gui_label = tk.Label(gui_main, text='Glup Any Key To Start!', bg='black', fg='white')
gui_label.place(relx=0.5, rely=0.5, anchor='center')
gui_label.pack(expand=1)

paddle_1 = tk.Canvas(gui_main, bg='white', height=100, width=10)
paddle_1.place(relx=0, rely=0.5, anchor=CENTER)

paddle_2 = tk.Canvas(gui_main, bg='white', height=100, width=10)
paddle_2.place(relx=1, rely=0.5, anchor=CENTER)

# listens for any 'KeyPress' event
gui_main.bind('<KeyPress>', onKeyPress)

# run the gui
gui_main.mainloop()
