num_str = "42"
num_int = int(num_str)  # Converts "42" to the integer 42
print(type(num_int))

num_str = "3.14"
num_float = float(num_str)  # Converts "3.14" to the float 3.14
print(type(num_float))

num_int = 42
num_str = str(num_int)  # Converts the integer 42 to the string "42"
print(type(num_int))

num_int = 42
bool_value = bool(num_int)  # Converts the non-zero integer to True
print(type(bool_value))

empty_list = []
bool_value = bool(empty_list)  # Converts the empty list to False
print(type(bool_value))

my_tuple = (1, 2, 3)
my_list = list(my_tuple)  # Converts the tuple (1, 2, 3) to the list [1, 2, 3]
print(type(my_list))

my_list = [1, 2, 3]
my_tuple = tuple(my_list)  # Converts the list [1, 2, 3] to the tuple (1, 2, 3)
print(type(my_tuple))

my_list = [1, 2, 2, 3]
my_set = set(my_list)  # Converts the list [1, 2, 2, 3] to the set {1, 2, 3}
print(type(my_set))

"""
Output :
<class 'int'>
<class 'float'>
<class 'int'>
<class 'bool'>
<class 'bool'>
<class 'list'>
<class 'tuple'>
<class 'set'>

"""