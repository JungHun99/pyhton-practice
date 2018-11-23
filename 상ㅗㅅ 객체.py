import math

class shape:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def area(self):
        print("계산할 수 없음")

    def perimeter(self):
        print("계산할 수 없음")

class rectangle(shape):
    def __init__(self,x,y,w,h):
        super().__init__(x,y)
        self.w=w
        self.h=h

    def area(self):
        return self.w*self.h

    def perimater(self):
        return 2*(self.w+self.h)

class circle(shape):
    def __init__(self,x,y,x1,y1):
        super().__init__(x,y)
        self.x1=x1
        self.y1=y1
        
    def area(self):
        return (self.x-self.x1)*(self.x-self.x1)*3.14

    def perimater(self):
        return 2*(abs(3.14*(self.x-self.x1)))


r=rectangle(0,10,50,200)

print("사각형면적",r.area())
print("사각형 둘레",r.perimater())

c= circle(0,20,10,30)

print("원의 넓이",c.area())
print("원의 둘레",c.perimater())
