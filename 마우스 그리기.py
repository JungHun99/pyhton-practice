#201811485
#정훈
#마우스 그리기
import turtle

t=turtle.Turtle()

def draw(x,y):
    t.goto(x,y)

t.screen.onclick(draw)
t.screen.listen()
