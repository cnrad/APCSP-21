#Draw the picture you created in the trifold at the beginning of this activity. 
#Make sure to add your name to submission title
#Add a picture of your drawing as a file so I can compare it to your code. :) 

import turtle as trtl
import math

v = trtl.Turtle()

# These are changeable! starting coords + size
initX = 0
initY = 0
unit = 12

v.pensize(3)
v.penup()

# Define function for drawing eyes so code isn't redundant
def draw_eye(x, y):

  # Set coords
  v.penup()
  v.setx(x)
  v.sety(y)
  v.pendown()
  
  # Pupil
  v.dot(3)
  
  # Eye circle
  v.penup()
  v.sety(y - unit)
  v.pendown()
  v.circle(1 * unit)
  
  
# Set pos
v.setx(initX)
v.sety(initY)

# Draw Square
v.pendown()
v.forward(7 * unit)
v.right(90)
v.forward(6 * unit)
v.right(90)
v.forward(7 * unit)
v.right(90)
v.forward(6 * unit)
v.right(90)

# Relative positioning for eyes
draw_eye(initX + (2 * unit), initY - (2 * unit))
draw_eye(initX + (7 * unit) - (2 * unit), initY - (2 * unit))

# Smile
v.penup()
v.setx(initX + unit)
v.sety(initY - (4 * unit))
v.pendown()
v.right(45)
v.forward((unit * math.sqrt(2)))
v.left(45)
v.forward(3 * unit)
v.left(45)
v.forward((unit * math.sqrt(2)))
v.penup() 

# Ta-da!
wn = trtl.Screen()
wn.mainloop()
