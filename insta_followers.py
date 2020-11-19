from instaloader import Instaloader, Profile
from tkinter import *
import threading
import time

username = input("Enter Instagram Username : ")
bg = 'black'
fg = 'white'


def load_data():
    while True:
        L = Instaloader()
        profile = Profile.from_username(L.context, username)
        foll.configure(text=str(profile.followers), font=("",60), fg=fg, bg=bg)
        time.sleep(5)


root = Tk()
root.title("Instagram Follower Counter")
root.config(bg=bg)

Label(root, text="Instagram Followers Count ", font=("", 50), fg=fg, bg=bg).pack()
Label(root, text=" @"+username, font=("",40), fg=fg, bg=bg).pack()
foll = Label(root)
foll.pack()
Label(root, text="Followers ", font=("",50), fg=fg, bg=bg).pack()
threading.Thread(target=load_data).start()
Label(root, text="Live", fg='red', font=("",40), bg=bg).pack(side='bottom')
root.mainloop()
