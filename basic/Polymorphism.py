class Car:
    def __init__(self, name, model):
        self.caraname = name
        self.carmodel = model

    def display(self):
        print(self.caraname)


class Animal:
    def __init__(self, name, color):
        self.animalaName = name
        self.animalColor = color

    def display(self):
        print(self.animalaName)


class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(self.name)


car = Car('Suzuki', 'ZMSJ15455A')
animal = Animal('Elephant', 'Black')
human = Human('Vikash', 26)

for item in (car, animal, human):
    item.display()
