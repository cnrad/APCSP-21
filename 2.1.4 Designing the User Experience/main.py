#################################################################################
#   a214_TR_incorporating_input_12.py
#   Example Solution: Adds the user's password to the authorization screen.
################################################################################
#   a214_simple_window1.py
#   A program creates a window on your screen using Tkinter.
import tkinter as tk

def test_my_button():
    password = ent_password.get()

    lbl2_password.config(text = f'Password entered: {password}')
    
    frame_auth.tkraise()

# main window
root = tk.Tk()
root.geometry("300x150")
root.title('Authorization')

frame_login = tk.Frame(root)
frame_login.grid(row=0, column=0, sticky='news')

lbl_username = tk.Label(frame_login, text='Username:', font='Helvetica')
lbl_username.pack()

ent_username = tk.Entry(frame_login, bd=2)
ent_username.pack(pady=5)

lbl_password = tk.Label(frame_login, text='Password:', font='Helvetica')
lbl_password.pack()

ent_password = tk.Entry(frame_login, bd=2, show='*')
ent_password.pack(pady=5)

btn_login = tk.Button(frame_login, text='Login', command=test_my_button)
btn_login.pack()

frame_auth = tk.Frame(root)
frame_auth.grid(row=0, column=0, sticky='news')

lbl2_password = tk.Label(frame_auth, text=f'Password:', font='Helvetica')
lbl2_password.pack()

frame_login.tkraise()

root.mainloop()