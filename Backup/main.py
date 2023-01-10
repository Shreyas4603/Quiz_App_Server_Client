import customtkinter as ctk
from tkinter import PhotoImage,Canvas
from tkinter import filedialog

import time

import customtkinter as ct
from tkinter import filedialog
import shutil
import os

#configure
bg = "#1a1a1c"
accent = "#c3083f"
text = "#fff6df"
secondary = "#c3083f"

root = ctk.CTk()




width = 700
height = 900
root.geometry(str(width)+"x"+str(height))
root.resizable(0, 0)
root.title("Title by team")
root.configure(fg_color=bg)

filename_arr = [""]

#configure

#global variable








#global variable











#functions

def create_quiz_function():
    pass


def slide_x(value):
    atrib.place(x=int(value))
    sl_x.configure(text="x=" + str(int(value)))
    print("x=", value)


def slide_v(value):
    atrib.place(y=int(value))
    sl_y.configure(text="y=" + str(int(value)))
    print("y=", value)


def size_w(value):
    atrib.configure(width=int(value))
    sl_w.configure(text=int(value))


def size_h(value):
    atrib.configure(height=int(value))
    sl_h.configure(text=int(value))



#functions


#main
welcome_text=ctk.CTkLabel(root,text="Welcome",font=("Bebas Neue",100),text_color=secondary)
welcome_text.place(x=196,y=0)

tag_line=ctk.CTkLabel(root,text="Q u i z  M a s t e r  3 0 0 0",font=("MOMCAKE",18),text_color=text)
tag_line.place(x=250,y=100)

create_quiz=ctk.CTkButton(root,text="Create Quiz",command=create_quiz_function,font=("Adobe Gothic Std B",30),fg_color=bg,text_color=text,hover_color=secondary,border_color=secondary,border_width=2,corner_radius=50)
create_quiz.place(x=259,y=189)


start_quiz=ctk.CTkButton(root,text="Start   Quiz",font=("Adobe Gothic Std B",30),width=190,fg_color=bg,text_color=text,hover_color=secondary,border_color=secondary,border_width=2,corner_radius=50)
start_quiz.place(x=259,y=248)
quick_quiz=ctk.CTkButton(root,text="Quick   Quiz",font=("Adobe Gothic Std B",30),width=190,fg_color=bg,text_color=text,hover_color=secondary,border_color=secondary,border_width=2,corner_radius=50)
quick_quiz.place(x=259,y=306)


#main

#dev tools - position and size

atrib = quick_quiz

# position slider
slider_x = ctk.CTkSlider(root, from_=0, to=width, number_of_steps=width, command=slide_x)
slider_x.place(x=100, y=580)

slider_v = ctk.CTkSlider(root, from_=0, to=height, number_of_steps=height, command=slide_v, orientation="vertical", )
slider_v.place(x=100, y=400)

sl_x = ctk.CTkLabel(root)
sl_x.place(x=191, y=550)

sl_y = ctk.CTkLabel(root)
sl_y.place(x=40, y=490)

# size slider
slider_w = ctk.CTkSlider(root, from_=0, to=width, number_of_steps=width, command=size_w)
slider_w.place(x=50, y=380)

slider_h = ctk.CTkSlider(root, from_=0, to=height, number_of_steps=height, command=size_h, orientation="vertical", )
slider_h.place(x=50, y=200)

sl_w = ctk.CTkLabel(root)
sl_w.place(x=191, y=350)

sl_h = ctk.CTkLabel(root)
sl_h.place(x=40, y=290)






root.mainloop()