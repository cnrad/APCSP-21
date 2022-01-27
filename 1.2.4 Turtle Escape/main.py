import turtle
import random 

turtle.setup(400, 400)
turtle.screensize(400, 400)
turtle.speed("fastest")

v = turtle.Turtle()
v.pensize(4)
length = 20

path_width = 20
walls = 30
pen_color = "black"

# Change these for lower/higher door or barrier chances
door_chance = 8
barrier_chance = 8

door_present = False

v.pencolor(pen_color)
turtle.hideturtle()

def draw_door():
    v.penup()
    v.forward(path_width)
    v.pendown()

def draw_barrier():
    v.left(90)
    v.forward(path_width)
    v.back(path_width)
    v.right(90)

for i in range(walls):
    if walls - i <= 4:
        v.forward(length)
    elif i > 4:
        for j in range(int(length / path_width)):
            door_choice = random.randint(0, door_chance)
            barrier_choice = random.randint(0, barrier_chance)
            if barrier_choice == barrier_chance and door_present:
                draw_barrier()
                door_present = False
            if door_choice == door_chance:
                draw_door()
                door_present = True
            else:
                v.forward(path_width)
    else:
        v.forward(length)
        

    if i % 2 == 0:
        length += path_width
    v.left(90)
    door_present = False
    
# p for player
p = turtle.Turtle()
p.pu()
p.goto(path_width/2, path_width/2)
p.shape("turtle")
p.shapesize(0.5)
p.pd()

def move_player_up():
    p.sety(p.ycor() + path_width)

def move_player_left():
    p.setx(p.xcor() - path_width)

def move_player_down():
    p.sety(p.ycor() - path_width)

def move_player_right():
    p.setx(p.xcor() + path_width)

wn = turtle.Screen() 
wn.onkeypress(move_player_up, "Up")
wn.onkeypress(move_player_left, "Left")
wn.onkeypress(move_player_down, "Down")
wn.onkeypress(move_player_right, "Right")

wn.listen()
wn.mainloop()