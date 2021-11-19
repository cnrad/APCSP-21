#2 In your ladybug program, re-use your spider-leg algorithm to add straight legs to the ladybug image. A possible variation of your ladybug image is shown in your textbook. *Make sure to use pseudocode.

# Initialize
import turtle as trtl
ladybug = trtl.Turtle()

# Draw legs first, so they are under the body
# Set variables used for the legs
legs = 6
leg_length = 55
angle = 25

# Set starting point + pen size
ladybug.pensize(5)
ladybug.penup()
ladybug.goto(0,-40)
ladybug.pendown()
n = 0

# Actually draw the legs 
while (n < legs):
    ladybug.goto(0,-40)
    ladybug.setheading(angle)
    ladybug.forward(leg_length)
    angle -= 25
    n += 1

    # If 3 legs are done, add to the angle to do the other side
    if n == 3:
        angle -= 105

# Reinitialize for body
ladybug.penup()
ladybug.goto(0, 0)
ladybug.setheading(0)

# Create ladybug head
ladybug.pendown()
ladybug.pensize(40)
ladybug.circle(5)

# and body
ladybug.penup()
ladybug.goto(0, -55) 
ladybug.color("red")
ladybug.pendown()
ladybug.pensize(40)
ladybug.circle(20)
ladybug.setheading(270)
ladybug.color("black")
ladybug.penup()
ladybug.goto(0, 5)
ladybug.pensize(2)
ladybug.pendown()
ladybug.forward(75)

# Config dots
num_dots = 1
xpos = -20
ypos = -55
ladybug.pensize(10)

# Draw two sets of dots
while (num_dots <= 2 ):
    ladybug.penup()
    ladybug.goto(xpos, ypos)
    ladybug.pendown()
    ladybug.circle(3)
    ladybug.penup()
    ladybug.goto(xpos + 30, ypos + 20)
    ladybug.pendown()
    ladybug.circle(2)

    # position next dots
    ypos = ypos + 25 
    xpos = xpos + 5
    num_dots = num_dots + 1

ladybug.hideturtle()

wn = trtl.Screen()
wn.mainloop()