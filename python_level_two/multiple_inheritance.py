#multiple inheritance
class ParentClass1():
    # Parent class definition
    def __init__(self):
        print("ParentClass1")

class ParentClass2():
    # Another parent class definition
    def __init__(self):
        print("ParentClass2")

class ChildClass(ParentClass1, ParentClass2):
    # Child class inheriting from both Animal and Mammal
    def __init__(self):
        ParentClass1.__init__(self)
        ParentClass2.__init__(self)
        print("ChildClass")

chilobj = ChildClass()
"""
output :
ParentClass1
ParentClass2
ChildClass

"""
