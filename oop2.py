class Person:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

    def display(self):
        print(f"My name is {self.name}.I am a {self.gender} of {self.age} years.")

myob=Person("Natasha Mbithe",18,"female")
myob.display()
myob2=Person("Derrick",24,"male")
myob2.display()