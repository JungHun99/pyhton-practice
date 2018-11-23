import random
import turtle

grade=[]

t1=turtle.Turtle()
t2=turtle.Turtle()

def line():
    l=turtle.Turtle()
    for i in range(2):
        l.pu()
        l.goto(-300,-100+(150*i))
        l.pd()
        l.fd(300-(100*i))
        l.lt(90)
        l.fd(100)
        l.rt(90)
        l.fd(250+(100*i))
    l.rt(90)
    l.fd(150)

def start():
    t1.shape('turtle')
    t2.shape('turtle')
    t1.pencolor('red')
    t2.pencolor('blue')
    t1.pu()
    t2.pu()
    t1.goto(-300,-50)
    t2.goto(-300,0)

def t1_right():
    t1.setheading(0)
    t1.fd(5)
    
def t1_left():
    t1.setheading(180)
    t1.fd(5)
    
def t1_up():
    t1.setheading(90)
    t1.fd(5)
    
def t1_down():
    t1.setheading(270)
    t1.fd(5)

def t2_right():
    t2.setheading(0)
    t2.fd(5)
    
def t2_left():
    t2.setheading(180)
    t2.fd()
    
def t2_up():
    t2.setheading(90)
    t2.fd(5)
    
def t2_down():
    t2.setheading(270)
    t2.fd(5)


line()
start()

t1.screen.onkeypress(t1_right,"f")
t1.screen.onkeypress(t1_left,"a")
t1.screen.onkeypress(t1_up,"d")
t1.screen.onkeypress(t1_down,"s")
t2.screen.onkeypress(t2_right,"l")
t2.screen.onkeypress(t2_left,"h")
t2.screen.onkeypress(t2_up,"j")
t2.screen.onkeypress(t2_down,"k")
t1.screen.listen()
t2.screen.listen()
if(t1.xcor()>250):
    t1.ht()
    grade.append('red')
if(t2.xcor()>250):
    t2.ht()
    grade.append('blue')
    
if(t1.isvisible()==0)and(t2.isvisible()==0):
    if(grade[0]=='red'):
        print("1등은 red 입니다")
        print("2등은 blue 입니다")
    else:
        print("1등은 blue 입니다")
        print("2등은 red 입니다")
