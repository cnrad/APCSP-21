# To play, use the arrow keys to navigate the player. 
# Whatever color the player is, navigate to the corresponding square before the time runs out. 
# The game will become increasingly more difficult as time goes on. Can you beat it?

import turtle
import random

# Define font setups for the timer and score
font_setup = ("Arial", 20, "normal")
font_setup_2 = ("Arial", 12, "normal")

# Setup window
turtle.screensize(400, 400)
turtle.setup(400, 400)

# Setup timer
text = turtle.Turtle() 
text.hideturtle()
text.pu() 
text.goto(-100, 140)
text.write("Starting game...", font=font_setup)

# Setup score turtle
score_turtle = turtle.Turtle() 
score_turtle.hideturtle()
score_turtle.pu() 
score_turtle.goto(-150, -150)
score_turtle.write("Score: 0", font=font_setup_2)

# Setup player
player = turtle.Turtle()
player.shape("circle")
player.shapesize(0.75)
player.penup() 
player.goto(0, 0)

# Initialize values
colors = ["red", "green", "blue", "yellow"]
corners = {} # Use a dictionary, not a list for the key:value format
step_size = 5
corner_size = 2
timer = 4
score = 0

# Countdown function
def countdown():
    global timer
    # If the timer is 0 then check the player position
    if timer == 0:
        check_player()
    else:
        # Rewrite timer
        text.clear()
        text.write("Time left: " + str(timer), font=font_setup)
        timer -= 1
        text.getscreen().ontimer(countdown, 1000) 

# Use enumerate() to access index and value when looping through list, to instantiate the corner turtles and add them to the dictionary
for i, v in enumerate(colors):
    corner = turtle.Turtle() 
    corner.shape("square")
    corner.shapesize(corner_size)
    corner.pu()
    corner.color(v)
    # Assign the turtle to it's color value in the dictionary
    corners[v] = corner

def random_color():
    player.color(random.choice(colors))

def check_player(): 
    # Fetch the player's coordinates, shape coordinates, and player color
    player_x = player.xcor()
    player_y = player.ycor()
    color = player.pencolor() 
    corner_x = corners[color].xcor()
    corner_y = corners[color].ycor()

    # Declare variables as global so we can change them inside the function scope
    global corner_size
    global score

    # Check player position in relation to the shape position
    if abs(corner_x - player_x) < (corner_size * 10) and abs(corner_y - player_y) < (corner_size * 10):
        # If they are in the range, change text and restart round
        text.clear()
        text.write("Good job!", font=font_setup)
        corner_size -= 0.2
        score += 10

        score_turtle.clear()
        score_turtle.write("Score: " + str(score), font=font_setup_2)

        play_round()
    else:
        # If they are out of the range, end the game
        text.clear()
        text.write("Game over!", font=font_setup)

# Function for changing size of all the shapes
def size_shapes():
    for e in colors:
        corners[e].shapesize(corner_size)
        corners[e].goto(random.randint(-150, 150), random.randint(-150, 150))

# Function for executing the round
def play_round():
    size_shapes()
    random_color()

    # Make the timer shorter based on the score
    global timer 
    if score > 60:
        timer = 2
    elif score > 40:
        timer = 3
    else:
        timer = 4

    # If the score is 100, they win the game
    if score != 100:
        countdown()
    else:
        text.clear()
        text.write("You win!", font=font_setup)

# Start game
play_round()

# PLayer movement methods
def move_player_up():
    player.sety(player.ycor() + step_size)

def move_player_left():
    player.setx(player.xcor() - step_size)

def move_player_down():
    player.sety(player.ycor() - step_size)

def move_player_right():
    player.setx(player.xcor() + step_size)

wn = turtle.Screen()  

# Event listeners
wn.onkeypress(move_player_up, "Up")
wn.onkeypress(move_player_left, "Left")
wn.onkeypress(move_player_down, "Down")
wn.onkeypress(move_player_right, "Right")

wn.listen()
wn.mainloop()