#if block
if 1<2 :
    print("true") # true

#nested if
if 1<2:
    print("first block")
    if 2 > 1:
        print("second block")

"""
output : 
first block
second block
"""
#if else
if 3 < 2 :
    print("if block")
elif 2 >= 2:
    print("else if  block")
else:
    print("else block")

"""
output : else if  block
"""
#for loop

list = [1,2,3,4,5,6]
for num in list:
    print(num) # 1 2 3 4 5 6 each in new lien

dic = {"name": "sudam", "age":30}
for item in dic:
    print(item) # name age each in new lien

for item in dic:
    print(dic[item]) # sudam 30 each in new lien

for item in dic.values():
    print(item) # sudam 30 each in new lien

#while loop
i=0
while i<5:
    print(i)
    i = i + 1 # 0 1 2 3 4 each in new lien

#Starting from python 3.10

x = 3
match x:
    case 1:
        print("Option 1")
    case 2:
        print("Option 2")
    case 3:
        print("Option 3")
    case _:
        print("Default option")

#output  : Option 3
