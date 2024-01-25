class Person:
    def __init__(self, fname, lName):
        self.firstname = fname
        self.lastname = lName

    def printName(self):
        print(self.firstname)
        print(self.lastname)


p = Person("Vikash", "Kumar")


# p.printName()


class Child(Person):
    def __init__(obj, contact, email):
        obj.phone = contact
        obj.mail = email
        # adding new property to student year
        obj.year = 2020

    def show(self):
        print(self.mail)
        print(self.year)
        super().__init__(self, "Child_name", "Child_l_name")


child = Child("8810271698", "vikash@email.com")
print("This output is from child class")
child.show()
child.printName()
