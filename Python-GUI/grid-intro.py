from tkinter import ttk
import tkinter as tk

def greet():
    #
    print(f"Hello, {user_name.get() or 'World'}!")

root = tk.Tk()

root.title("Greeter Box")

root.columnconfigure(0,weight=1)

user_name = tk.StringVar()

input_frame = ttk.Frame(root,padding=(20,10,20,0))
input_frame.grid(row=0,column=0,sticky="EW")

name_label = ttk.Label(input_frame,text='Name:')
name_label.grid(row=0,column=0)

name_entry = ttk.Entry(input_frame,width=15,textvariable=user_name)
name_entry.grid(row=0,column=1)
name_entry.focus()

button_frame = ttk.Frame(root,padding=(20,10))
button_frame.grid(sticky="EW")

button_frame.columnconfigure(0,weight=1)
button_frame.columnconfigure(1,weight=1)

greet_button = ttk.Button(button_frame,text="Greet",command=greet)
greet_button.grid(row=0,column=0,sticky="EW")

quit_button = ttk.Button(button_frame,text="Quit",command=root.destroy)
quit_button.grid(row=0,column=1,sticky="EW")

root.mainloop()