"""
Tuples are a built-in data type in Python used to store an ordered collection of items.
They are similar to lists in many ways, but they have some key differences.
The main characteristics of tuples are:
* Immutable: Tuples are immutable, meaning once they are created, their elements
           cannot be modified, added, or removed.
           However,you can create a new tuple with updated values.

* Ordered: Tuples maintain the order of elements, and you can access elements using their index.

* Heterogeneous Data: Tuples can store elements of different data types, such as integers, strings, floats, or even other tuples.

* Creation: Tuples are defined using parentheses () or by using the tuple() constructor.

* Since tuples are immutable, functions that modify elements (e.g., append, pop, remove) are
  not available for tuples
"""
my_tuples = (1,2,"sudam",[1,2,3])
my_tuples2 = (1,2,3,4,5)
print(my_tuples) #(1, 2, 'sudam', [1, 2, 3])
print(my_tuples[0]) # 1
# my_tuples[0] = 5  TypeError: 'tuple' object does not support item assignment
print(len(my_tuples)) #4
print(max(my_tuples2)) #5
print(min(my_tuples2)) # 1
print(my_tuples.count(2)) # 1
print(my_tuples.index(2)) #1
print(my_tuples + my_tuples2) #(1, 2, 'sudam', [1, 2, 3], 1, 2, 3, 4, 5)
print(my_tuples * 2) # (1, 2, 'sudam', [1, 2, 3], 1, 2, 'sudam', [1, 2, 3])
