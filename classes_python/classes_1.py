class Dog(object):

    def __init__(self, name, age, weight) -> None:
        self.name = name
        self.age = age
        self.weight = weight 
        print('Nice you mad a dog class')


    def speak(self):
        print(f"Hi my name is self.name {self.name} and my age is {self.age}" )
    

    def add_weight(self):
        print (f"check my weight {self.weight}")



tim = Dog('Vini', 26, 100)
fred = Dog('Sophia', 10, 90)

tim.speak()
fred.speak()

tim.add_weight()

print(tim.weight)