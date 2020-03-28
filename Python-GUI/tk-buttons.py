#!/usr/bin/env python3

from tkinter import ttk
import tkinter as tk


def greet():
    #
    print("Hello World!")

root = tk.Tk()

# Widgets #

greet_button = ttk.Button(root, text="Greet", command=greet)

quit_button = ttk.Button(root, text="Quit", command=root.destroy)

# Expand is used to fill excess horizontal space

greet_button.pack(side="left",fill="x",expand=True)

# fill = both can be used to take up all space for each container

quit_button.pack(side="right",fill="y")

# Pack will anchor elements to the top of the container or 
# the bottom of the previous element

root.mainloop()

