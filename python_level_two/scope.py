# local
f = lambda x:x**2  # here x is local variable
x = 50
def func(x):
    print('x is', x)
    x = 2
    print('Changed local x to', x)

func(x)
print('x is still', x)

"""
output :
x is 50
Changed local x to 2
x is still 50
"""

# enclosing functions

name = 'This is a global name'
def greet():
    # Enclosing function
    name = 'Sammy'
    def hello():
        print('Hello '+name)
    hello()

greet() #output Hello Sammy
# global
x = 50
def funcglobal():
    global x
    print('global x is: ', x)
    x = 2
    print('changed global x to', x)

print('Before calling function x is: ', x)
funcglobal()
print('After calling function x is: ', x)

"""
Output :
Before calling function x is:  50
global x is:  50
changed global x to 2
After calling function x is:  2

"""
# built-in