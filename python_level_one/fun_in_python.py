#function without param
def my_fun():
    print("welcome")

my_fun() #welcome

#function with param
def test(param = "default"):
    print(param)

test() #default
test("hello") #hello

#function with return
def calculation(num1,num2):
    if type(num1)==type(num2)==type(10):
        return num1 + num2
    else:
        return "Sorry, integer value required"

result = calculation("hello",3)
print(result) # Sorry, integer value required
result = calculation(2,3)
print(result) # 5

#filter
def is_even(num):
    return num % 2 == 0

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filtered_numbers = filter(is_even, numbers)
even_numbers = list(filtered_numbers)

print(even_numbers) # Output: [2, 4, 6, 8, 10]

#lambda Expression
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filtered_numbers = filter(lambda num:num%2==0, numbers)
even_numbers = list(filtered_numbers)
print(even_numbers) # Output: [2, 4, 6, 8, 10]

#in oprater in python
print('y' in [1,2,3,4]) # false
print('y' in [1,2,3,'y']) #true