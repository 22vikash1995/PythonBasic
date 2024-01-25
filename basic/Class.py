# class with one property
class Animal:
    author = "Vikash"


object1 = Animal()
print(object1.author)


# class with _init_() method
class Test:
    def __init__(self, name, age, contact):
        self.name = name
        self.age = age
        self.contact = contact


obj = Test("vikash", "26", "8810271698")
print(obj)


# method in a class
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def my_fun(self):
        print("My Name is:", self.name)
        print("My Age is:", self.age)


student = Student("Vikash", 26)
student.name="Vicky"
student.my_fun()
