from tkinter import ttk
import tkinter as tk

root = tk.Tk()
root.geometry("600x400")
root.resizable(False,False)
root.title("Widgets - Scrollbar")

root.grid_columnconfigure(0,weight=1)
root.grid_rowconfigure(0,weight=1)

text = tk.Text(root,height=8)
text.grid(row=0,column=0,sticky="EW")

text.insert("1.0","Please enter a comment-> ")

text_scroll = ttk.Scrollbar(root, orient="vertical",command=text.yview)

text_scroll.grid(row=0,column=1,sticky="NS")

text["yscrollcommand"] = text_scroll.set

root.mainloop()