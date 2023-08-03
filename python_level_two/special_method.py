class Book():

    def __init__(self,name,author,pages):
        self.name = name
        self.author = author
        self.pages = pages

    # Method called when the this class object printed.
    def __str__(self):
        return "Title : {}, Author : {}, Pages : {}".format(self.name,self.author,self.pages)

    # Method called when the this class object used in len method
    def __len__(self):
        return self.pages

    # Method called when the this class object deleted
    def __del__(self):
        print('Book Object is destroyed.')

my_book = Book('Python','Rahul Dhamecha',300)
print(my_book) # Title : Python, Author : Rahul Dhamecha, Pages : 300
print(len(my_book)) #300
del my_book #Book Object is destroyed.