# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 16:19:09 2017

@author: kunalprince
"""

from Tkinter import *
import Tkinter

root=Tkinter.Tk()
frame = Tkinter.Frame(root)
frame.pack()

topFrame = Tkinter.Frame(root)
middleFrame = Tkinter.Frame(root)
bottomFrame = Tkinter.Frame(root)

topFrame.place(relx=0.5, rely=0.5, anchor=CENTER)
middleFrame.place(height=200, width=500, x=50, y=20)
bottomFrame.place(height=100,width=500)

major=Label(topFrame,text="Major Project on")
heading=Label(topFrame, text="Stress Detection in Automobile Drivers")

major.place(height=50, width=500)
heading.place(height=50, width=500)

major.pack()
heading.pack()

root.mainloop()