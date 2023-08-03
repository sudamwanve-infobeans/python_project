# base class
class Animal():
    def __init__(self):
        print("From Animal class")

    def whoAmI(self):
        print("animal")

    def eat(self):
        print("Eating")

#derived Class
class Dog(Animal):

    def __init__(self):
        Animal.__init__(self)
        print('DOG CREATED')

    def bark(self):
        print('WOOF WOOF!')

    def eat(self):
        print('DOG EATING')


dog = Dog() #DOG CREATED
dog.whoAmI()  # Result : animal
dog.eat()  # Result : DOG EATING
dog.bark()  # Result : WOOF WOOF!
