import turtle as trtl

#----- maze and turtle config variables
screen_h = 400
screen_w = 420
startx = -100
starty = -100
turtle_scale = 1.5

#------ robot commands
def move():
    robot.dot(10)
    robot.fd(50)

def turn_left():
    robot.speed(0)
    robot.lt(90)
    robot.speed(2)

#----- init screen
wn = trtl.Screen()
wn.setup(width=screen_w, height=screen_h)
robot_image = "./sprites/robot.gif"
wn.addshape(robot_image)

#----- init robot
robot = trtl.Turtle(shape=robot_image)
robot.hideturtle()
robot.color("darkorchid")
robot.pencolor("darkorchid")
robot.penup()
robot.setheading(90)
robot.turtlesize(turtle_scale, turtle_scale)
robot.goto(startx, starty)
robot.speed(2)
robot.showturtle()

wn.bgpic("./sprites/maze2.png")

# Begin robot movement

# ROUTE 1

# Move forward (up 3)
i = 0
while i < 3:
    move()
    i += 1

# Turn left 3 times (270deg)
i = 0
while i < 3:
    turn_left()
    i += 1

# Move forward (left 2)
i = 0
while i < 2:
    move()
    i += 1

# RESET STARTING POSITION
robot.goto(startx, starty)

# ROUTE 2

# Define j and set to 0
j = 0

# First while loop defines the repeated motion (forward 3, turn left)
while j < 2:
    # Reset i to 0 on every iteration
    i = 0

    # Move forwards 3 times, and then turn left
    while i < 3:
        move() 
        i += 1
    turn_left() 

    # Increment j
    j += 1

    # If j is 2 (indicating the final iteration has finished), move forward once to the gray square
    if j == 2:
        move()

# End robot movement 
wn.mainloop()