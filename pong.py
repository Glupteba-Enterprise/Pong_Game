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



# setting gui variables
gui_main.title(gui_title)
gui_main.geometry(f'{gui_width}x{gui_height}+{gui_x}+{gui_y}')  # width x height ± x ± y

# key press detector. will be used for 'press any key to start game'
def onKeyPress(event):
    """sets the 'on key press' text"""
    gui_text_var.insert('end', f'You pressed {(event.char, )}\n')

# shows text on screen
gui_text_var = tk.Text(gui_main, background='black', foreground='white', font=('Comic Sans MS', 12))
gui_text_var.pack()

# listens for any 'KeyPress' event
gui_main.bind('<KeyPress>', onKeyPress)
# run the gui
gui_main.mainloop()
