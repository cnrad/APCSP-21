#3 In your spider program, use the circle and setheading methods in an iteration/looping algorithm to draw curved legs on a bug instead of straight ones.
#Add a head to the spider by drawing a smaller circle close to the body of the spider and change the eye location. A possible variation of your spider image is shown in the text; yours may look quite different. *Make sure to use pseudocode.

# Initialize
import turtle as trtl
spider = trtl.Turtle()
spider.pensize(3)
spider.speed(10)

# Define variables
center = (0, 10) # using tuples for easier coords :)
leg_count = 8
leg_angle = 20
leg_curve = 7
leg_length = 80

# Draw the legs
i = 0
while i < leg_count:
    # Reset leg curve each leg
    leg_curve = 10
    # Return to center
    spider.penup()
    spider.goto(center)
    spider.pendown()

    # Draw one leg (8 segments, I wanted to create my own algorithm as a challenge rather than using the partial circle method)
    for j in range(8):
        spider.setheading(leg_angle + (5 * leg_curve))
        spider.forward(leg_length / 8)
        # Change curve direction based on the leg iteration (first 4 or last 4)
        if i > 3:
            leg_curve += 3 
        else:
            leg_curve -= 3 

    # Change leg angle direction based on the leg iteration (first 4 or last 4)
    if i < 3:
        leg_angle -= 25
    else:
        leg_angle += 25

    # Increment iteration count
    i += 1
    if i == leg_count / 2:
        # If 4th leg is done, draw them on the other side
        leg_angle -= 270

# Draw the body
# Return to center coords
spider.penup()
spider.goto(center)
spider.pendown()
spider.pensize(60)
# Draw a small circle with a large pensize to center it around the point
spider.circle(1)
spider.penup()

# Draw the head
# Move down from body
spider.sety(spider.ycor() - 35)
spider.pendown()
spider.pensize(30)
spider.circle(1)
spider.penup()

# Draw the spider's very evil eyes
spider.sety(spider.ycor() - 5)
for i in range(2):
    # -5 on first iteration, 5 on second
    spider.setx(-5 if i == 0 else 5)
    spider.pendown()
    spider.pencolor("red")
    spider.pensize(5)
    spider.circle(1)
    spider.penup()

wn = trtl.Screen()
wn.mainloop()