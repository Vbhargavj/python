from tkinter import *
from PIL import Image,ImageTk

root = Tk()

photo = None

try:
    image=Image.open("vbj.jpg")
    
    photo =ImageTk.PhotoImage(file="vbj.jpg")
except TclError as e:
    print(f"Error: {e}")

if photo:
    label = Label(root, image=photo)
    label.pack()

root.mainloop()