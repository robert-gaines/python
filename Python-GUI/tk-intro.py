#! /usr/bin/env python3

import tkinter as tk
from tkinter import ttk

'''
 Test tkinter
 tkinter._test()
'''

root = tk.Tk() # TK Object

ttk.Label(root, text="Hello World!", padding=(50,50)).pack()

root.mainloop()
