#201811485
#정훈
#동전
import random
import turtle
t = turtle.Turtle()

color = ["red", "blue"]
world=["앞","뒤"]
dice = int(input("몇번 던지겠습니까?"))
b = [0,0]

for i in range(dice):
    x = random.randint(0,1)
    if(x==0):
        b[0] = b[0]+1
    elif(x==1):
        b[1] = b[1]+1


for i in range(2):
    print("동전",world[i],"면", b[i], "번")

for c in range(2):
    t.pu()
    t.goto(-200,c*-50)
    t.pd()
    t.pencolor(color[c])
    t.width(20)
    t.fd(b[c]*5)
    t.pu()
    t.fd(20)
    t.write(b[c], move=False, align="left", font=("Arial", 10, "normal"))
    t.backward(20)
    t.pd()
    
t.ht()
