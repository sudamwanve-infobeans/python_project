def my_decorators(func):
    def wrap_func():
        print("Wrap Function Called!")
        func()
        print("func() function is called!")
    return wrap_func
@my_decorators # decorator called
def decorator_function():
    print('Decorator function called.')

decorator_function()

"""
Output :
Wrap Function Called!
Decorator function called.
func() function is called!

"""