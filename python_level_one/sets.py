"""
1. Sets can only contain unique elements
2. Sets are unordered, which means they do not
   maintain the order in which elements are added
3. Sets are created using curly braces {} or by using the set() constructor
"""
# Creating a set
my_set = {1, 2, 3, 4}
# Creating an empty set
empty_set = set()
print(empty_set) # set()
# add element in sets by usimg add method
my_set.add(5)
print(my_set) #{1, 2, 3, 4, 5}
#remove element
my_set.remove(3)
print(my_set)#{1, 2, 4, 5}
my_set.discard(2)
print(my_set) #{1, 4, 5}
#opration on set
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1.union(set2)
print(union_set)# {1, 2, 3, 4, 5}
intersection_set = set1.intersection(set2)
print(intersection_set)# {3}
difference_set = set1.difference(set2)
print(difference_set)# {1, 2}
symmetric_difference_set = set1.symmetric_difference(set2)
print(symmetric_difference_set)# {1, 2, 4, 5}