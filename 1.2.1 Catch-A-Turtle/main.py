# Extra feature: certain % chance to get a blue circle, which gives you 5 seconds of additional time if clicked

# a121_catch_a_turtle.py

#----- Import Statements-----
import turtle as trtl
import random as rand

#----- Game Configuration ----
v_color = "red"
v_size = 2
v_shape = "circle"

font_setup = ("Arial", 16, "normal")

score = 0
timer = 30
counter_interval = 1000  # 1000 represents 1 second
timer_up = False

bonus_chance = 15 # Change to have a 1 in (x) chance of bonus time

#----- Initialize Turtle -----
v = trtl.Turtle()
score_writer = trtl.Turtle()
counter =  trtl.Turtle()

#----- Game Functions ------
score_writer.penup()
score_writer.hideturtle()
score_writer.goto(115, 100)

counter.penup()
counter.hideturtle()
counter.goto(-200, 100)

v.color(v_color)
v.shapesize(v_size)
v.shape(v_shape)
v.penup()

def v_clicked(x: int, y: int):
    global timer_up

    if timer_up == False:
        # Execute game functions
        update_score()
        change_position()
        
        # If the color was blue the previous time, add bonus time, and then reset color
        if v.pencolor() == "blue":
            bonus_time()

        # Reset to original color
        v.color(v_color)

        # Random chance to change color to blue and add extra time for next click
        if rand.randint(1, bonus_chance) == 5:
            v.color("blue")

    else:
        # End game
        print("Game over!")
        v.hideturtle() 
        counter.hideturtle()
        counter.clear()

        score_writer.clear()
        score_writer.goto(-75, 0)
        score_writer.write(f"Final Score: {score}", font=font_setup)

def change_position():
    x = rand.randint(-100, 100)
    y = rand.randint(-100, 100)
    v.goto(x, y)

def update_score():
    global score
    score += 1
    score_writer.clear()
    score_writer.write(f"Score: {score}", font=font_setup)

def countdown():
    global timer, timer_up
    counter.clear()
    if timer <= 0:
        counter.write("Time's Up", font=font_setup)
        timer_up = True
    else:
        counter.write("Timer: " + str(timer), font=font_setup)
        timer -= 1
        counter.getscreen().ontimer(countdown, counter_interval) 

def bonus_time():
    global timer
    timer += 5 # Add x amount of seconds to the timer

#----- Events ------
wn = trtl.Screen()
wn.setup(500, 300) # Change window size as well
wn.ontimer(countdown, counter_interval) 
v.onclick(v_clicked)
wn.mainloop()