import praw
import time
import webbrowser
import tkinter as tk
from tkinter import filedialog
root = tk.Tk()
root.withdraw()
webbrowser.open_new("https://www.reddit.com/prefs/apps")
time.sleep(2)
tk.messagebox.showwarning('Alert', """Set up a Script at the bottom of this page, and get your information to input into the form in the script!""")
reddit = praw.Reddit(client_id=input("Client ID: "), client_secret=input("Client Secret: "), user_agent='kjhgfgbhjifdnbc vghnjfd', username=input("Username: "), password=input("Password: "))
excluded_subs = []
while True:
    for comment in reddit.user.me().comments.new(limit=None):
        comment.delete()
        print(f"Comment deleted! - {comment}")
