#object oriented programming
class Fruits:
    def __init__(self,name,price,number):
        self.name = name
        self.price =price
        self.number = number

    def onyesha(self):
        print(f"I love eating {self.name} that costs {self.price}.I can eat {self.number} of them.")

myob=Fruits("bananas",40,6)
myob.onyesha()
myob2=Fruits("pineapples",100,2)
myob2.onyesha()