#   a116_ladybug.py
import turtle as trtl

# create ladybug head
ladybug = trtl.Turtle()
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

# config dots
num_dots = 1
xpos = -20
ypos = -55
ladybug.pensize(10)

# draw two sets of dots
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
  ypos = ypos + 25 # error 1: defining xpos instead of ypos with ypos variable (error: typo)
  xpos = xpos + 5
  num_dots = num_dots + 1 # error 2: defining a NEW variable (num_dot) instead of redefining num_dots (error: typo)

ladybug.hideturtle()

wn = trtl.Screen()
wn.mainloop()

#Record and explain the errors you found with this program.  

    # The program ran infinitely and kept drawing the dots in the same place

# Describe in your own words why the errors occurred and how you fixed them.

    # The errors were just simple typos with variable declarations:

        #   - Line 42: xpos = ypos + 25 ---> should be defining ypos, not xpos
        #          Because of this error, the y position wasn't changing, and it kept resetting to draw the dots in the same place

        #   - Line 44: num_dot = num_dots + 1 ---> should be num_dots, not num_dot
        # Because of this error, num_dots never incremented and the condition in the while loop was never met (it checks num_dots, not num_dot), allowing the program to run infinitely