# Given a list of integers, return True if the sequence of numbers 1, 2, 3
# appears in the list somewhere.

# For example:
# arrayCheck([1, 1, 2, 3, 1]) → True
# arrayCheck([1, 1, 2, 4, 1]) → False
# arrayCheck([1, 1, 2, 1, 2, 3]) → True

def findseq(nums):
    i = 0
    while i < len(nums) - 2:
        if nums[i] == 1 and nums[i+1] == 2 and nums[i+2] == 3:
            return True
        i += 1
    return False

print(findseq([1, 1, 2, 3, 1]))  # Output: True
print(findseq([1, 1, 2, 4, 1]))  # Output: False
print(findseq([1, 1, 2, 1, 2, 3]))  # Output: True


# Given a string, return a new string made of every other character starting
# with the first, so "Hello" yields "Hlo".

# For example:
# stringBits('Hello') → 'Hlo'
# stringBits('Hi') → 'H'
# stringBits('Heeololeo') → 'Hello'

def mystring(str):
  result = ""
  for i in range(len(str)):
    if i % 2 == 0:
      result = result + str[i]
  return result

result = mystring("hello");
print(result);#hlo
result = mystring("hi");
print(result);#H
result = mystring("Heeololeo");
print(result);#Hello

# Given two strings, return True if either of the strings appears at the very end
# of the other string, ignoring upper/lower case differences (in other words, the
# computation should not be "case sensitive").
#
# Note: s.lower() returns the lowercase version of a string.
#
# Examples:
#
# end_other('Hiabc', 'abc') → True
# end_other('AbC', 'HiaBc') → True
# end_other('abc', 'abXabc') → True
def end_other(a, b):
    a = a.lower()
    b = b.lower()

    return a.endswith(b) or b.endswith(a)

print(end_other('Hiabc', 'abc'))  # Output: True
print(end_other('AbC', 'HiaBc'))  # Output: True
print(end_other('abc', 'abXabc'))  # Output: True

# Given a string, return a string where for every char in the original,
# there are two chars.

# doubleChar('The') → 'TThhee'
# doubleChar('AAbb') → 'AAAAbbbb'
# doubleChar('Hi-There') → 'HHii--TThheerree'

def doubleChar(str):
  result = ''
  for char in str:
    result += char * 2
  print(result)

doubleChar('The') #'TThhee'
doubleChar('AAbb') #'AAAAbbbb'
doubleChar('Hi-There') #'HHii--TThheerree'

# Read this problem statement carefully!

# Given 3 int values, a b c, return their sum. However, if any of the values is a
# teen -- in the range 13-19 inclusive -- then that value counts as 0, except 15
# and 16 do not count as a teens. Write a separate helper "def fix_teen(n):"that
# takes in an int value and returns that value fixed for the teen rule.
#
# In this way, you avoid repeating the teen code 3 times (i.e. "decomposition").
# Define the helper below and at the same indent level as the main no_teen_sum().
# Again, you will have two functions for this problem!
#
# Examples:
#
# no_teen_sum(1, 2, 3) → 6
# no_teen_sum(2, 13, 1) → 3
# no_teen_sum(2, 1, 14) → 3

def fix_teen(n):
    if 13 <= n <= 19 and n not in [15, 16]:
        return 0
    return n

def no_teen_sum(a, b, c):
    a = fix_teen(a)
    b = fix_teen(b)
    c = fix_teen(c)
    return a + b + c

print(no_teen_sum(1, 2, 3))  #  6
print(no_teen_sum(13, 14, 15))  #  15
print(no_teen_sum(16, 17, 18))  #  16

# Return the number of even integers in the given array.
#
# Examples:
#
# count_evens([2, 1, 2, 3, 4]) → 3
# count_evens([2, 2, 0]) → 3
# count_evens([1, 3, 5]) → 0

def count_evens(nums):
  count = 0
  for element in nums:
    if element % 2 == 0:
      count += 1
  print(count)

count_evens([2, 1, 2, 3, 4]) # 3
count_evens([2, 2, 0]) # 3
count_evens([1, 3, 5]) # 0