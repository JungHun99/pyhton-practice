import turtle
import random
import time

player = turtle.Turtle()
player.shape("turtle")
player.up()

score = turtle.Turtle()
score.ht()
score.up()
score.goto(300,300)

def make(count,feed):
    for i in range(count):
        f=turtle.Turtle()
        f.shape("circle")
        f.up()
        f.goto(random.randint(-300,300),random.randint(-300,300))
        feed.append(f)
    return feed

feed=[]
feed = make(20,feed)
count=0

def left():
    global player
    player.lt(15)

def right():
    global player
    player.rt(15)

score.write("score : "+str(count))

while(1):
    player.fd(10)
    turtle.onkeypress(left,"Left")
    turtle.onkeypress(right,"Right")
    for f in range(len(feed)):
        if(15>((player.xcor()-feed[f].xcor())**2+((player.ycor()-feed[f].ycor())**2))**0.5):
            feed[f].ht()
            score.clear()
            score.write("score : "+str(count))
            count+=1
            del(feed[f])
            break

    if(len(feed)<10):
        feed=make(10,feed)

    time.sleep(0.05)
    turtle.listen()
