from tkinter import *
import random
import time

tk = Tk()
tk.title("Game")
tk.resizable(0, 0)
canvas = Canvas(tk, width=450, height=400, bd=0, highlightthickness=0)
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
        self.id=self.canvas.create_oval(self.x,self.y,self.x+15,self.y+15,fill=self.color)

    def move(self):
        self.canvas.move(self.id,self.x1,self.y1)
        self.x+=self.x1
        self.y+=self.y1

    def hit(self):
        if(self.x<0):
            self.x1=2
        elif(self.y<0):
            self.y1=2
        elif(self.x>435):
            self.x1=-2

    def  paddle_hit(self,xp,yp):
        if(self.y>yp-10 and self.y<yp):
            if(xp-10 < self.x and xp+90 > self.x):
                self.y1=-random.randint(1,3)

    def gety(self):
        return self.y
    
    def getpos(self):
        return self.canvas.coords(self.id)

    def block_hit(self):
        if(self.y1>0):
            self.y1=-2
        else:
            self.y1=2

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


class block:
    def __init__(self,canvas, color_count, i):
        self.canvas=canvas
        self.color_list=["red","yellow","green"]
        self.color_count=color_count
        self.i=i
        self.block_id= self.canvas.create_rectangle((self.i%15)*30,(self.i//15)*10,((self.i%15)+1)*30,((self.i//15)+1)*10,fill=self.color_list[color_count-1])
        time.sleep(0.01)
        tk.update()

    def checking(self,pos):
        if((self.canvas.coords(self.block_id)[0]<pos[0] and self.canvas.coords(self.block_id)[2]>pos[0]) or (self.canvas.coords(self.block_id)[0]<pos[2] and self.canvas.coords(self.block_id)[2]>pos[2])):
            if((self.canvas.coords(self.block_id)[3]>pos[3] and self.canvas.coords(self.block_id)[1]<pos[3])or(self.canvas.coords(self.block_id)[3]>pos[1] and self.canvas.coords(self.block_id)[1]<pos[1])):
                self.color_count-=1
                if(self.color_count==0):
                    self.canvas.delete(self.block_id)
                    return 1
                else:
                    self.canvas.itemconfig(self.block_id,fill=self.color_list[self.color_count-1])
                    return 2
        return 0
        
while(1):
    dif=int(input("난이도를 선택해주세요(1: 하 2: 중 3: 상 4: 종료)"))
    if(dif>0 and dif<4):
        break
    elif(dif==4):
        exit()
    else:
        print("다시 골라 주세요")

for i in range(3):
    print(3-i,"초 뒤에 실행됩니다.")
    time.sleep(1)
    
ball=ball(canvas,"gray",random.randint(100,150),100)
paddle=paddle(canvas,"blue",200,300)
block=[block(canvas,random.randint(1,dif),i) for i in range(30)]
tk.update()

while(1):
    if(len(block)==0):
        break
    canvas.bind_all('<KeyPress-Left>', paddle.left)
    canvas.bind_all('<KeyPress-Right>',paddle.right)
    ball.move()
    paddle.move()
    ball.hit()
    xp,yp=paddle.getxy()
    ball.paddle_hit(xp,yp)
    a=ball.getpos()
    che=0
    for block_c in block:
        try:
            imit=block_c.checking(a)
            if(imit==1):
                ball.block_hit()
                del block[che]
            elif(imit==2):
                ball.block_hit()
        except:
            break
        che+=1
    tk.update()
    if( ball.gety() >390):
        break
    time.sleep(0.01)
    tk.update()
