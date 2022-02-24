# a213_pw_analyzer.py
import time
import pwalgorithms as pwa

password = input("Enter password:")

print("Analyzing password ...")
time_start = time.time()

# attempt to find password + password method used
found, num_guesses = pwa.one_word(password)
time_end = time.time()

# report results
if (found):
    print(password, "found in", num_guesses, "guesses")
else: 
    # check two word
    found, num_guesses = pwa.two_word(password)

    if (found):
        print(password, "found in", num_guesses, "guesses")
    else: 
        # check two word and digit
        found, num_guesses = pwa.two_words_and_digit(password)

        if (found):
            print(password, "found in", num_guesses, "guesses")
        else: 
            # check two word and digit and character
            found, num_guesses = pwa.two_words_digit_character(password)

            if (found):
                print(password, "found in", num_guesses, "guesses")
            else:
                # no method found the password
                print(password, "NOT found in", num_guesses, "guesses!")
print("Time:", format((time_end-time_start), ".8f"))