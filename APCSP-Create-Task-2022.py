import turtle
import random

# VARIABLES + PROGRAM SETUP

# Setup window
turtle.screensize(400, 400)
turtle.setup(400, 400)

# Initialize variables
font_setup = ("Arial", 14, "normal")
alphabet = "abcdefghijklmnopqrstuvwxyz"
word_list = ["established", "celebration", "faithful", "dictate", "flourish", "expression", "biography", "excuse"]

# List to store ALL of the guessed letters
guessed_letters = []
# List to store incorrectly guessed letters only (that are not in the word)
incorrect_letters = []

# Setup instruction text turtle
instruction_text = turtle.Turtle() 
instruction_text.hideturtle()
instruction_text.pu() 
instruction_text.goto(-150, 150)
instruction_text.write("Press any key to guess a letter!", font=font_setup)

# Setup guessed letters text turtle
guessed_drawer = turtle.Turtle() 
guessed_drawer.hideturtle()
guessed_drawer.pu()
guessed_drawer.goto(-160, -140)

# Setup the turtle for drawing the canvas
v = turtle.Turtle()
v.speed("fastest")
v.hideturtle()
v.pu()
v.goto(-160, 100)


# FUNCTION DECLARATIONS

# Function that draws the main canvas
def draw_canvas(word):

    # Draw spaces for letters
    for i in word:
        v.pd()
        v.setx(v.xcor() + 20)
        v.pu()
        v.setx(v.xcor() + 10)

    # Draw the hanger for the man
    v.goto(-50, -100)
    v.pd()
    v.sety(30)
    v.setx(20)
    v.sety(20)
    v.pu()

# Function that draws each part of the man based on the number of letters missed
def draw_man(number):
    v.pd()
    
    # Draw head
    if number == 1:
        v.setheading(180)
        v.circle(10)
        v.setheading(0)

    # Draw body
    if number == 2:
        v.setheading(270)
        v.pu()
        v.forward(20)
        v.pd()
        v.forward(50)

    # Draw right arm
    if number == 3:
        v.pu()
        v.setheading(90)
        v.forward(40)
        v.setheading(-45)
        v.pd()
        v.forward(25)
        v.backward(25)

    # Draw left arm
    if number == 4:
        v.setheading(225)
        v.forward(25)
        v.backward(25)

    # Draw right leg
    if number == 5:
        v.pu()
        v.setheading(-90)
        v.forward(40)
        v.setheading(-45)
        v.pd()
        v.forward(25)
        v.backward(25)

        # Draw left leg
    if number == 6:
        v.setheading(225)
        v.forward(25)
    
    v.pu()

# Function that takes the letter the user guessed
def letter_guessed(letter):
    if letter in guessed_letters: # If the user already guessed it
        return print("You already guessed that!")

    # Add the letter to the guessed_letters list and rewrite it
    guessed_letters.append(letter)
    guessed_drawer.clear()
    guessed_drawer.write("Guessed: " + ', '.join(guessed_letters), font=font_setup)
    
    if letter in word: # If the letter IS in the word
        # Get the indices at which the guessed letter appears in the word
        letter_indices = [i for i, c in enumerate(word) if c == letter]
        print(f"{letter} is in the word {len(letter_indices)} times!")
        
        # Setup letter drawing turtle
        letter_drawer = turtle.Turtle() 
        letter_drawer.hideturtle()
        letter_drawer.pu() 
        letter_drawer.sety(100)

        # Draw the letters in the word
        for j in letter_indices:
            letter_drawer.setx(-155 + (j * 30))
            letter_drawer.write(letter, font=font_setup)

        # If all the letters in the word are guessed
        if all(guessed_letters.count(letter) > 0 for letter in word) == True:
            v.clear()
            # Write the full word, and the user wins
            word_text = turtle.Turtle() 
            word_text.pu()
            word_text.goto(-175, 0)
            word_text.write(f"You win! The word was {word}", font=font_setup)
            print(f"You win! The word was {word}")
            
    else: # If the letter IS NOT in the word
        print(f"{letter} is not in the word!")
        incorrect_letters.append(letter)
        draw_man(len(incorrect_letters))

        if len(incorrect_letters) >= 6:
            v.clear()
            # Write the word, and the user loses
            word_text = turtle.Turtle() 
            word_text.pu()
            word_text.goto(-175, 0)
            word_text.write(f"You lose! The word was {word}", font=font_setup)
            print(f"You lose! The word was {word}")

            
# PROGRAM START
            
# Choose a random word from word_list
word = random.choice(word_list)
# Tell the program to draw the board, and pass word as an argument so it knows how many spaces to draw
draw_canvas(word)

wn = turtle.Screen() 

# For every letter in the alphabet list, create a wn.onkeypress listener
for letter in alphabet:
    # When the letter is pressed, call the letter_guessed function with the letter passed as an argument
    wn.onkeypress(lambda k=letter: letter_guessed(k), letter)

wn.listen()
wn.mainloop()
