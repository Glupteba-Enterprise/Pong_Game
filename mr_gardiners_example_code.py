	import random
2	from tkinter import *
3
4	def mouse_clicked(event):
5	    global bob
6	    print(event.x, event.y)
7	    print(canvas.find_overlapping(event.x, event.y, event.x, event.y))
8	    if bob in canvas.find_overlapping(event.x, event.y, event.x, event.y):
9	        print("you hit bob")
10	        canvas.itemconfig(bob, fill=f"#{random.randint(0,0xFFFFFF):06x}")
11	        canvas.delete(bob)
12	        window.after(1000, create_bob)
13	    else:
14	        print("you missed bob")
15
16	def create_bob():
17	    global bob
18
19	    bob = canvas.create_rectangle(x, y, x + width, y + height, fill="blue")
20	    move_stuff()
21	def move_stuff():
22	    global x_vel, y_vel, bob
23	    canvas.move(bob, x_vel, y_vel)
24	    if canvas.coords(bob)[2] > 800 or canvas.coords(bob)[0] < 0:
25	        x_vel = -x_vel
26	    if canvas.coords(bob)[3] > 600 or canvas.coords(bob)[1] < 0:
27	        y_vel = -y_vel
28
29	    window.after(16, move_stuff)
30
31
32	window = Tk()
33	canvas = Canvas(window, width="800", height="600", background="blanchedalmond")
34	canvas.pack()
35	# canvas.create_rectangle(100, 100, 200, 200, fill="blue")
36
37
38	x_vel = 1
39	y_vel = 1
40	x = 100
41	y = 100
42	width = 100
43	height = 100
44	bob = canvas.create_rectangle(x, y, x + width, y + height, fill="blue")
45	move_stuff()
46	canvas.bind("<Button-1>", mouse_clicked)
47	window.mainloop()