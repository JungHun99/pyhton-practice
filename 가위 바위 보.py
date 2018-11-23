#201811485
#정훈
#가위 바위 보
import random
import turtle
t = turtle.Turtle()

color = ["red", "blue","black"]
world=["가위","바위","보"]
game = int(input("몇번 하시겠습니까?"))
b = [0,0,0]

for i in range(game):
    x = random.randint(0,2)
    if(x==0):
        b[0] = b[0]+1
    elif(x==1):
        b[1] = b[1]+1
    elif(x==2):
        b[2] = b[2]+1

for i in range(3):
    print("주사위",world[i],"는", b[i], "번")

for c in range(3):
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
