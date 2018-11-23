#201811485
#정훈
#주사위 확률
import random
import turtle
t = turtle.Turtle()

color = ["black", "blue", "red", "yellow", "green", "pink"]

dice = int(input("몇번 던지겠습니까?"))
b = [0,0,0,0,0,0]

for i in range(dice):
    dice = random.randint(1,6)
    b[dice-1] = b[dice-1]+1

i = 0
for i in range(6):
    print("주사위",i+1,"면", b[i], "번")
    i=+1

for c in range(6):
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
