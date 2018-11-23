from tkinter import *
import time
import random

pos=[-3,-2,-1]
pos1=[1,2,3]

x=2
y=2

paddlemove=0

xl=0
yl=0

xp=200
yp=300

tk=Tk()
tk.resizable(0,0)
canvas=Canvas(tk,width=500,height=400,bd=0, highlightthickness=0)
canvas.pack()
tk.update()

ball=canvas.create_oval(0,0,15,15,fill="red")
paddle=canvas.create_rectangle(0,0,100,10,fill="blue")
canvas.move(paddle,xp,yp)

def hit():
    global x,y
    if(xl<0):
        x=pos1[1]
    elif(yl<0):
        y=pos1[1]
    elif(xl>480):
        x=pos[1]
    

def hit_paddle():
    global xp,yp,xl,yl,y
    if(yl>yp-10):
        if(xp-10 < xl and xp+90 > xl):    
            y=pos[1]

def left(evt):
    global paddlemove
    paddlemove=-2

def right(evt):
    global paddlemove
    paddlemove=2

while(1):
    canvas.bind_all('<KeyPress-Left>', left)
    canvas.bind_all('<KeyPress-Right>',right)
    xl+=x
    yl+=y
    xp+=paddlemove
    canvas.move(ball,x,y)
    canvas.move(paddle,paddlemove,0)
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)
    hit_paddle()
    hit()
    if(yl>390):
        break





















