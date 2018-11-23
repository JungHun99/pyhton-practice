class animal:
    def __init__(self,name):
        self.name=name

    def say():
        print("알 수 없음")


class dog(animal):
    def __init__(self,name):
        super().__init__(name)

    def say():
        print("멍멍")


class cat(animal):
    def __init__(self,name):
        super().__init__(name)

    def say(animal):
        print("야옹야옹")


animalList=[dog(dog1),dog(dog2)]

for a in animalList:
    print(a.name+':'+a.say())
        
