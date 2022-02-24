# a213_multi_factor.py
import tkinter as tk
import multifactorgui as mfg
import os # using for environment variables

# create a multi-factor interface to a restircteownlo app
my_auth = mfg.MultiFactorAuth()

# set the users authentication information
question = "What is your favorite song without the first letter?"
answer = os.environ.get('ANSWER')
my_auth.set_authentication(question, answer)
my_auth.set_authorization("admin", os.environ.get('ADMIN_PASS'))

# start the GUI
my_auth.mainloop()