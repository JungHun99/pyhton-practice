from tkinter import *
import random
import time

tk = Tk()
tk.title("Game")
tk.resizable(0, 0)
canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
canvas.pack()
tk.update()

class ball:
    def __init__(self, canvas,color,x,y):
        self.canvas = canvas
        self.color=color
        self.x1=2
        self.y1=2
        self.x=x
        self.y=y
        self.id=canvas.create_oval(self.x,self.y,self.x+15,self.y+15,fill=self.color)

    def move(self):
        self.canvas.move(self.id,self.x1,self.y1)
        self.x+=self.x1
        self.y+=self.y1

    def hit(self):
        if(self.x<0):
            self.x1=2
        elif(self.y<0):
            self.y1=2
        elif(self.x>485):
            self.x1=-2

    def  paddle_hit(self,xp,yp):
        if(self.y>yp-10 and self.y<yp):
            if(xp-10 < self.x and xp+90 > self.x):
                self.y1=-2

    def gety(self):
        return self.y

class paddle:
    def __init__(self,canvas,color,x,y):
        self.canvas = canvas
        self.color=color
        self.paddlemove=0
        self.x=x
        self.y=y
        self.id=canvas.create_rectangle(0,0,100,10,fill="blue")
        canvas.move(self.id,self.x,self.y)

    def move(self):
        self.canvas.move(self.id,self.paddlemove,0)
        self.x+=self.paddlemove

    def right(self,evt):
        self.paddlemove=2

    def left(self,evt):
        self.paddlemove=-2

    def getxy(self):
        return self.x,self.y
        
        
    
ball=ball(canvas,"gray",100,100)
paddle=paddle(canvas,"blue",200,300)
tk.update()
while(1):
    canvas.bind_all('<KeyPress-Left>', paddle.left)
    canvas.bind_all('<KeyPress-Right>',paddle.right)
    ball.move()
    paddle.move()
    ball.hit()
    xp,yp=paddle.getxy()
    ball.paddle_hit(xp,yp)
    tk.update()
    if( ball.gety() >390):
        break
    time.sleep(0.01)
    
