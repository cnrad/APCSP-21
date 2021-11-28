# Modify the code to change the color of turtles, delete colors available to the turtles, add more turtles, and change program parameters to see the results.

import turtle as trtl

# Create an empty list of turtles
my_turtles = []

# Use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
turtle_colors = ["red", "blue", "green", "orange", "purple", "gold"]

for s in turtle_shapes:
    # Instantiate turtle
    t = trtl.Turtle(shape=s)

    # Remove the color and assign it to a variable, because List.pop() method returns the removed item
    current_color = turtle_colors.pop()
    t.color(current_color)

    # Add it to the list
    my_turtles.append(t)

# Initialize the variables for the turtle to use (position, direction)
startx = 0
starty = 0
heading = -45

# Iterate through the turtle instance list
for t in my_turtles:
    # Pen up when going to location, and pen down afterwards
    t.penup()
    t.goto(startx, starty)
    t.pendown()

    # Set turtle angle and move forward
    t.right(heading)     
    t.forward(50)

    # Change angle for next turtle
    heading += 45

    # Set the position of the next turtle to the coordinates of the current one
    startx = t.xcor()
    starty = t.ycor()

# Create screen and start event loop
wn = trtl.Screen()
wn.mainloop()