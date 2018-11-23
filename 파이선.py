import turtle as t
import random

dice=[]
diceNum=[]

number=int(input("주사위를 몇번 던지겠습니까? "))

for i in range(number):
    r= random.randint(1,6)
    dice.append(r)

for i in range(6):
    diceNum.append(dice.count(i+1))

for i in range(6):
    print(diceNum[i])

t.shape('turtle')
t.lt(90)
t.fd(200)
t.goto(0,0)
t.rt(90)
t.fd(300)
t.goto(0,0)
t.ht()

def graph():
    t.fd(20)
    t.pencolor('black')
    t.pu()
    t.rt(90)
    t.fd(20)
    t.write(str(i+1)+"번")
    t.backward(20)
    t.lt(90)
    t.pd()
    t.pencolor(color[i])
    t.begin_fill()
    t.fillcolor(color[i])
    t.lt(90)
    t.fd(diceNum[i]*5)
    t.write(diceNum[i])
    t.rt(90)
    t.fd(30)
    t.rt(90)
    t.fd(diceNum[i]*5)
    t.lt(90)
    t.end_fill()


color=['red','purple','blue','black','green','orange']

for i in range(6):
    graph()
