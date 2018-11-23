import turtle
import random

tur=[]
color=['red','blue','orange','pink','black','purple','green']
grade=[]

racer=int(input("선수가 몇명인지 입력하시오(최대 7명)"))
distance=int(input("한번의 최대거리를 입력하시오"))
line=int(input("몇m 거리 경기인지 입력하시오"))

dis=turtle.Turtle()
dis.color('red')

def turtle_race(racer,dist,line):
    g=1
    for i in range(racer):
        r1=turtle.Turtle()
        r1.shape('turtle')
        r1.pencolor(color[i])
        r1.pu()
        r1. goto(-200,200-(50*i))
        tur.append([r1,color[i]])
        
    dis.pu()
    dis.goto(-200+line,-300)
    dis.pd()
    dis.goto(-200+line,300)
    dis.ht()

    while(1):
        for i in tur:
            i[0].fd(random.randint(0,dist))
            if (i[0].xcor()>-200+line):
                k=i
                grade.append(i[1])
                i[0].ht()
                g+=1
                if(g==racer):
                    break
                
        for i in range(racer):
            print(str(i+1)+"등:"+ grade(g))
        
turtle_race(racer,distance,line)
