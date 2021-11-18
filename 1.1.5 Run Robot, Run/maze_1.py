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

wn.bgpic("./sprites/maze1.png")

# Begin robot movement

# Move forward (up 5)
i = 0
while i < 4:
    move()
    i += 1

# Turn left 3 times (270deg)
i = 0
while i < 3:
    turn_left()
    i += 1

# Move forward (left 5)
i = 0
while i < 4:
    move()
    i += 1

# End robot movement 

wn.mainloop()