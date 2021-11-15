# Draw a sketch of the picture.
# ./sketch.png

# Identify the shapes, dimensions, and /or colors that the user will specify during runtime.
# Hat color, hat height, picture size


#### CODE ####

import turtle as trtl
import iridi # A Python package I created a while ago to make console input/print look kinda cool :)

v = trtl.Turtle()

hat_color: str = iridi.input("What color would you like the hat to be?\n", ["#00c3ff", "#ffff1c"], italic=True, bold=True)
height: int = int(iridi.input("How tall would you like the hat to be?\n", ["#fc00ff", "#00dbde"], italic=True, bold=True))
unit: int = int(iridi.input("How big would you like the hat man to be?\n", ["#feac5e", "#c779d0", "#4bc0c8"], italic=True, bold=True)) / 10

iridi.presets.wiretap.print("\nEnjoy :)")

# Define a rectangle method to make things easier
def rect(l: int, w: int):
  # Initial direction 
  v.setheading(270)
  for i in range(4):
    # Move forward length if i is odd, width if i is even
    v.forward(l) if i % 2 == 1 else v.forward(w)
    v.left(90)

v.pensize(3)

v.circle(unit * 5)
v.penup()

# Eyes
v.setx(unit * -2)
v.sety(unit * 6)
v.pendown()
v.dot(3)
v.penup()

v.setx(unit * 2)
v.sety(unit * 6)
v.pendown()
v.dot(3)
v.penup()

# Mouth
v.sety(unit * 3)
v.pendown()
v.setx(unit * -2)
v.penup()

# Hat
v.setx(unit * -5)
v.sety(unit * 11)
v.pendown()
v.color(hat_color)
v.begin_fill()
rect(unit * 10, unit * 3)
v.end_fill()

v.setx(unit * -3)
v.sety((unit * height) + (unit * 11))
v.pendown()
v.begin_fill()
rect(unit * 6, unit * height)
v.end_fill()

# Nice little man in a hat is finished
wn = trtl.Screen()
wn.mainloop()

################

# How well did your program match your sketch?

# It matched up pretty well