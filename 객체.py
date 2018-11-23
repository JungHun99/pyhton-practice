from turtle import*

class Car:
    def __init__(self,speed,color,model):
        self.speed=speed
        self.model=model
        self.color=color
        self.turtle=Turtle()
        self.turtle.shape("C:/th.gif")

    def drive(self):
        self.turtle.forward(self.speed)

    def pre(self,speed):
        self.speed+=speed

    def left_turn(self):
        self.turtle.left(90)


register_shape("C:/th.gif")
myCar=Car(100,"red","E-class")
for i in range(100):
    myCar.drive()
    myCar.left_turn()
    myCar.pre(2)
        
