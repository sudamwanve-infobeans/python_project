#class and object
class Dog():
    species = 'mammal'
    def __init__(self,breed,name):
        self.breed = breed
        self.name = name

sam = Dog('Lab','Sam')

print(sam.name) #output -> Sam

#second Example of class and object
class Circle():
    pi = 3.14

    # instantiated
    def __init__(self, radius=1):
        self.radius = radius

    # method
    def area(self):
        return self.radius * self.radius * Circle.pi

    def setRadius(self, radius):
        self.radius = radius

    def getRadius(self):
        return self.radius


c = Circle()

c.setRadius(2)
print ('Radius is: ',c.getRadius())
print ('Area is: ',c.area())

"""
Output :
Radius is:  2
Area is:  12.56

"""