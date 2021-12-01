# I just noticed you removed the 1.1.8 module so I'm not sure if we're supposed to do this but I did it anyways

# ----------------

#Try to implement the extra features outlined in the textbook.
#I have made adjustments so your turtles will not fly off the screen.
#I have put how to change the screen size and background color if you would like to experiment with that.
#speed up and slow down turtles 
#change color and shape during a collision #recover their originalshape and color when the keep on moving.
'''10 Points
Speed- 4
Change Color- 4
Recover- 2'''

#  a118_turtles_in_traffic.py
#  Move turtles horizontally and vertically across screen.
#  Stopping turtles when they collide.

# ----------------

import random # will be used for randomizing speeds
import turtle as trtl
trtl.screensize(canvwidth=500, canvheight=500, bg="yellow")
print(trtl.screensize())

# Create two empty lists of turtles, adding to them later
horiz_turtles = []
vert_turtles = []

# Create an empty list we will use to store the turtle's speeds
speeds = []

# Use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
horiz_colors = ["red", "blue", "green", "orange", "purple", "gold"]
vert_colors = ["darkred", "darkblue", "lime", "salmon", "indigo", "brown"]

tloc = -40

for s in turtle_shapes:
    ht = trtl.Turtle(shape=s)
    horiz_turtles.append(ht)
    ht.penup()
    new_color = horiz_colors.pop()
    ht.fillcolor(new_color)
    ht.goto(-150, tloc)
    ht.setheading(0)

    vt = trtl.Turtle(shape=s)
    vert_turtles.append(vt)
    vt.penup()
    new_color = vert_colors.pop()
    vt.fillcolor(new_color)
    vt.goto(-tloc+50, 200)
    vt.setheading(270)
    tloc += 40

    # Randomize speeds for the array, between 1 and 5
    speeds.append(random.randint(1, 5))

# Move turtles across and down screen, stopping for collisions

steps = 0
while steps < 50:

    # Use enumerate() method so we can access both the element as well as index in the loop 
    for index, htl in enumerate(horiz_turtles):
        for index2, vtl in enumerate(vert_turtles):

            # If turtles xcor AND ycor are less than 20, remove them from the list
            if abs(htl.xcor() - vtl.xcor()) < 20 and abs(htl.ycor() - vtl.ycor()) < 20:
                horiz_turtles.remove(htl) 
                vert_turtles.remove(vtl)

            # Move forward by the speed at the index (between 1 and 5 steps)
            htl.forward(speeds[index])
            vtl.forward(speeds[index2 - 2]) # switch up the speeds a bit so they aren't the same between htl and vtl

    # Increment steps
    steps = steps + 1
 
wn = trtl.Screen()
wn.mainloop()