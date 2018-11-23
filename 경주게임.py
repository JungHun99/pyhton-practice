import random
import turtle

grade=[]

t1=turtle.Turtle()
t2=turtle.Turtle()

#경기 라인을 만드는 함수
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

#선수를 시작점으로 만드는 함수
def start():
    t1.shape('turtle')
    t2.shape('turtle')
    t1.pencolor('red')
    t2.pencolor('blue')
    t1.pu()
    t2.pu()
    t1.goto(-300,-50)
    t2.goto(-300,0)

#선수 조작 함수
def t1_right():
    t1.setheading(0)
    
def t1_left():
    t1.setheading(180)
    
def t1_up():
    t1.setheading(90)
    
def t1_down():
    t1.setheading(270)

def t2_right():
    t2.setheading(0)
    
def t2_left():
    t2.setheading(180)
    
def t2_up():
    t2.setheading(90)
    
def t2_down():
    t2.setheading(270)


line()
start()

#이동을 반복적으로 돌리면서 방향만 바꿈 선수 두명이 다 통과해야 종료
while(1):
    t1.fd(random.randint(1,5))
    t2.fd(random.randint(1,5))
    t1.screen.onkeypress(t1_right,"d")
    t1.screen.onkeypress(t1_left,"a")
    t1.screen.onkeypress(t1_up,"w")
    t1.screen.onkeypress(t1_down,"s")
    t2.screen.onkeypress(t2_right,"Right")
    t2.screen.onkeypress(t2_left,"Left")
    t2.screen.onkeypress(t2_up,"Up")
    t2.screen.onkeypress(t2_down,"Down")
    t1.screen.listen()
    t2.screen.listen()
    #출발선을 넘어가면 터틀을 지우고 리스트에 저장 
    if(t1.xcor()>250):
        t1.ht()
        grade.append('red')
    if(t2.xcor()>250):
        t2.ht()
        grade.append('blue')
    if(t1.isvisible()==0)and(t2.isvisible()==0):
        break

#리스트 확인후 1등 2등 출력
if(grade[0]=='red'):
    print("1등은 red 입니다")
    print("2등은 blue 입니다")
else:
    print("1등은 blue 입니다")
    print("2등은 red 입니다")
