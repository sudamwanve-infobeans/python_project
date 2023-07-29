#string declartion
fname="sudam"
lname='wanve'
print(fname) #sudam
print(lname) #wanve
print(fname[0])  #s
print(fname[-1]) #m
print(fname[:5])  # sudam
print(fname[1:5])  # udam
print(fname[::3])  # sa
name = 'Sudam haridas Wanve'
print(name.upper())  # SUDAM HARIDAS WANVE (Converts the string to uppercase.)
print(name.lower())  # sudam haridas wanve (Converts the string to lowercase.)
print(name.casefold())  # sudam haridas wanve
print(name.capitalize())  # Sudam haridas wanve (only first letter capitalize)
print(name.encode())  # b'Sudam haridas Wanve'
print(name.count('a'))  # 4
print(name.count('a', 1, 5))  # 1
print(name.center(30))  #  Sudam haridas Wanve
print(name.center(30, '*'))  # *****Sudam haridas Wanve******
splitval = name.split() #split string
print(splitval)   #['Sudam', 'haridas', 'Wanve']
#how print string
print(name)
newname = "Hello {} {}".format(name, "welcome")
print(newname);
print(len(name)) # Returns the length of the name.
print(name.strip()) # Removes leading and trailing whitespace from the name.
print(name.replace("sudam", "badam")) # Replaces all occurrences of 'old' with 'new' in the name.
print(name.startswith('su')) # Returns True if the name starts with the specified 'prefix'.
print(name.endswith('ve')) # Returns True if the name ends with the specified 'suffix'.
print(name.isalpha()) # Returns True if all characters in the name are alphabetic.
print(name.isdigit()) # Returns True if all characters in the name are digits.
print(name.isalnum()) # Returns True if all characters in the name are alphanumeric.
print(name.islower()) # Returns True if all characters in the name are lowercase.
print(name.isupper()) # Returns True if all characters in the name are uppercase.
print(name.title()) # Converts the first character of each word to uppercase and the rest to lowercase.
print(name.find("su")) # Returns the lowest index of the first occurrence of 'subname' in the name.
print(name.isnumeric())# Returns True if all characters in the name are numeric.
"""
output from len () to isnumeric()
19
Sudam haridas Wanve
Sudam haridas Wanve
False
True
False
False
False
False
False
Sudam Haridas Wanve
-1
False
"""


