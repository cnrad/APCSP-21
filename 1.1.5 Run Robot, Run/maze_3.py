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

wn.bgpic("./sprites/maze3.png")

# Begin robot movement

# It says I should use MULTIPLE nested inner loops, so I'm splitting it up into half (first move to first square, second move to last square) instead of having 4 consecutive moves, changing color on certain iteration

# Make the move to the square, twice
k = 0
while k < 2:
    # Reset i to 0
    i = 0
    # Repeat the same move twice
    while i < 2:
        j = 0

        # Move once, turn left 3 times, move once, turn left once
        while j < 6:
            if j % 4 == 0:
                move()
            elif j == 5:
                turn_left()
            else:
                turn_left()

            # Increment iteration count
            j += 1


        # Increment iteration count
        i += 1

    # Change color at the end of the first iteration so it shows on the second iteration
    robot.color("red")
    robot.pencolor("red")
    k += 1
            

# End robot movement 
wn.mainloop()