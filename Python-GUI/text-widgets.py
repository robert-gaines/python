from tkinter import ttk
import tkinter as tk

def ProduceText():
    #
    print(text_content)

root = tk.Tk()
root.geometry("600x400")
root.resizable(False,False)
root.title("Widgets")

text = tk.Text(root,height=8)
text.pack()

text.insert("1.0", "Enter text here-> ")

# text["state"] = "disabled"
# text["state"] = "normal"

# Starting index: 1.0 
# Last index: "end"

text_content = text.get("1.0","end")


produce_text_button = tk.Button(root,text="Produce Text",command=ProduceText)
produce_text_button.pack()

print(text_content)

root.mainloop()