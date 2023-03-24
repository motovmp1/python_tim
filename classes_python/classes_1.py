class Dog(object):

    def __init__(self, name) -> None:
        self.name = name
        print('Nice you mad a dog class')

    def speak(self):
        print("Hi my name is", self.name)


tim = Dog('Vini')
fred = Dog('Sophia')

tim.speak()
fred.speak()