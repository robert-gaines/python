#!/usr/bin/env python3

from tkinter import ttk
import tkinter as tk

root = tk.Tk()
main = ttk.Frame(root)
main.pack(side="left",fill="both",expand=True)

tk.Label(root,text="Label Top",bg="green").pack(side="top",expand="True",fill="both")
tk.Label(root,text="Label Top",bg="blue").pack(side="top",expand="True",fill="both")
tk.Label(root,text="Label Left",bg="yellow").pack(side="left",expand=True,fill="both")

root.mainloop()