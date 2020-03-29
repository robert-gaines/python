#from windows import set_dpi_awareness
#from PIL import Image,ImageTK
from tkinter import ttk
import tkinter as tk

#set_dpi_awareness()

root = tk.Tk()
root.geometry("600x400")
root.resizable(False,False)
root.title("Widget Intro")

greeting = tk.StringVar()
greeting.set("Hello User")

label = ttk.Label(root,text="Widget Intro",padding=(20,20))
label.config(font=("Segoe UI", 20))
label.pack()

#image=Image.open("").resize((64,64))
#photo = ImageTK.PhotoImage(image)
#label = ttk.Label(root,text="image with text",image=Photo,padding=5,compound="right")
#label["image"] = photo



root.mainloop()