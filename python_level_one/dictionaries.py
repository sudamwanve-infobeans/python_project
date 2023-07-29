#Dictionaries
"""
* dictionaries are a built-in data type used to store collections of key-value pairs.
  Dictionaries are also known as associative arrays or hash maps in other programming languages.
* Creation: Dictionaries are created using curly braces {} or by using the dict() constructor.
* Key-Value Pairs: Each item in a dictionary consists of a key and its associated value,
  separated by a colon :. Keys must be unique and can be of any immutable data type
  (e.g., strings, integers, tuples), while values can be of any data type.
* Accessing Values: You can access the value of a specific key by using the
   key inside square brackets [].
"""
my_stuff={"name": "sudam","age":30,"address": "pune"}
print(my_stuff) #{'name': 'sudam', 'age': 30, 'address': 'pune'}
print(my_stuff['name']) #sudam
my_stuff['name']='ganesha'
print(my_stuff) #{'name': 'ganesha', 'age': 30, 'address': 'pune'}
my_stuff={"name": "sudam","age":30,"address": "pune","marks" : {"english":20, "marathi": 90}}
print(my_stuff['marks']['marathi']) #90

#methods
print(my_stuff.keys()) #dict_keys(['name', 'age', 'address', 'marks'])
print(my_stuff.values()) #dict_values(['sudam', 30, 'pune', {'english': 20, 'marathi': 90}])
print(my_stuff.items()) #dict_items([('name', 'sudam'), ('age', 30), ('address', 'pune'), ('marks', {'english': 20, 'marathi': 90})])
print(my_stuff.pop('lastname', "not found key last name")) #not found key last name
print(my_stuff.popitem()) #('marks', {'english': 20, 'marathi': 90})
print(len(my_stuff)) #3
print(my_stuff.clear()) #None

"""
Iterating Over Dictionaries: You can use a for loop to iterate 
over the keys, values, or key-value pairs of a dictionary.
"""
my_stuff={"name": "sudam","age":30,"address": "pune"}
# Iterating over keys
for key in my_stuff:
    print(key) #name age address
# Iterating over values
for value in my_stuff.values():
    print(value) # sudam 30 pune

# Iterating over key-value pairs
for key, value in my_stuff.items():
    print(key, value)

"""
name sudam
age 30
address pune
"""
"""
Dictionary Comprehensions: Like lists, you can use dictionary comprehensions 
to create dictionaries in a concise way.
"""
squares = {x: x*x for x in range(1, 6)}
print(squares)# Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}