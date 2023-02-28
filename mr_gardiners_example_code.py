import random
from tkinter import *

def mouse_clicked(event):
    global bob
    print(event.x, event.y)
    print(canvas.find_overlapping(event.x, event.y, event.x, event.y))
    if bob in canvas.find_overlapping(event.x, event.y, event.x, event.y):
        print("you hit bob")
        canvas.itemconfig(bob, fill=f"#{random.randint(0,0xFFFFFF):06x}")
        canvas.delete(bob)
        window.after(1000, create_bob)
    else:
        print("you missed bob")

def create_bob():
    global bob

    bob = canvas.create_rectangle(x, y, x + width, y + height, fill="blue")
    move_stuff()
def move_stuff():
    global x_vel, y_vel, bob
    canvas.move(bob, x_vel, y_vel)
    if canvas.coords(bob)[2] > 800 or canvas.coords(bob)[0] < 0:
        x_vel = -x_vel
    if canvas.coords(bob)[3] > 600 or canvas.coords(bob)[1] < 0:
        y_vel = -y_vel

    window.after(16, move_stuff)


window = Tk()
canvas = Canvas(window, width="800", height="600", background="blanchedalmond")
canvas.pack()
# canvas.create_rectangle(100, 100, 200, 200, fill="blue")


x_vel = 1
y_vel = 1
x = 100
y = 100
width = 100
height = 100
bob = canvas.create_rectangle(x, y, x + width, y + height, fill="blue")
move_stuff()
canvas.bind("<Button-1>", mouse_clicked)

window.mainloop()
