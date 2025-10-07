'''
import tkinter

window = tkinter.Tk()
window.geometry('420x420')# size of a window
window.title("First GUI Window")# change title
window.config(background="#321ae8")# change bg window
window.mainloop()
'''


'''
from tkinter import *

root = Tk()
l1=Label(root,text="Hell Yeah! Kya Baat Kya Baat")
l1.pack()
root.mainloop()
'''


import tkinter as tk

root = tk.Tk()
root.title("Label Example")
root.geometry("420x420")
label = tk.Label(root, text="Welcome to Gotham City!", font=("Arial Bold", 25))
label.pack(pady=20)
root.mainloop()
