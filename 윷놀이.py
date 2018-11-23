#201811485
#정훈
#윷놀

import random
import turtle
t = turtle.Turtle()

color = ["black", "blue", "red", "yellow", "green","pink"]
world=["도","빽도","개","걸","윷","모"]
mid=[]

dice = int(input("몇번 던지겠습니까?"))
b = [0,0,0,0,0,0]

for i in range(dice):
    x = random.randint(0,1)
    y = random.randint(0,1)
    z = random.randint(0,1)
    d = random.randint(0,1)
    mid.append([x,y,z,d])

for x in range(dice):
    k=mid[x].count(0)
    if(k==1):
        if(mid[x][3]==0):
            b[0] = b[0]+1
        else:
            b[1] = b[1]+1
    elif(k==2):
        b[2] = b[2]+1
    elif(k==3):
        b[3] = b[3]+1
    elif(k==4):
        b[4] = b[4]+1
    elif(k==0):
        b[5] = b[5]+1

for c in range(6):
    t.pu()
    t.goto(-200,c*-50)
    t.pd()
    t.pencolor(color[c])
    t.width(20)
    t.fd(b[c]*5)
    t.pu()
    t.fd(20)
    t.write(world[c]+str(b[c]), move=False, align="left", font=("Arial", 10, "normal"))
    t.backward(20)
    t.pd()
    
t.ht()
