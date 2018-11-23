class cards:
    def __init__(self,simbol,number,bag):
        self.simbol=simbol
        self.number=number
        self.bag=bag

    def back(self):
        return self.bag

    def frount(self):
        return self.simbol, self.number


card=cards("diamond",7,"check")

print(card.back())
print(card.frount())
