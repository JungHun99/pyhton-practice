'''
from tkinter import*
import time

tk=Tk()
canvas=Canvas(tk,width=300,height=300)
canvas.pack()
poly1=canvas.create_polygon(10,10,10,60,50,35)

while (True):
    for i in range(0,60):
        canvas.move(poly1,3,3)
        tk.update()
        time.sleep(0.05)

    for i in range(0,60):
        canvas.move(poly1,-3,-3)
        tk.update()
        time.sleep(0.05)
        '''

from turtle import *

def ball:
    def __init__(self,color,size, speed):
        self.x=0
        self.y=0

        self.xspeed=speed
        self.yspeed=speed
        self.size=size
        self.color=color
        self.turtle=Turtle()

