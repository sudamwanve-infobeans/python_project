#list
list_one = [1,2,3]
list_two =["first","second",'1',2, [3,4,5]]
print(list_one) # [1, 2, 3]
print(list_two) # ['first', 'second', '1', 2, [3, 4, 5]]
print(list_one[0]) # 1
print(list_one[1:]) # [2, 3]
print(list_one[::]) # [1, 2, 3]
print(list_two[4])  # [3, 4, 5]
print(list_two[4][2]) # 5
print("list methods output")
#method of list
list = [1,2,3,4,5,5,6,7,8]
list2 =[11,12]
list.append(10)
print(list) #[1, 2, 3, 4, 5, 5, 6, 7, 8, 10]
list.extend(list2)
print(list) # [1, 2, 3, 4, 5, 5, 6, 7, 8, 10, 11, 12]
list.insert(0,13)
print(list) #[13, 1, 2, 3, 4, 5, 5, 6, 7, 8, 10, 11, 12]
list.remove(1)
print(list) #[13, 2, 3, 4, 5, 5, 6, 7, 8, 10, 11, 12]
list.pop(len(list)-1)
print(list) #[13, 2, 3, 4, 5, 5, 6, 7, 8, 10, 11]
print(list.index(3)) #2
print(list.count(5)) #2
list.sort()
print(list) #[2, 3, 4, 5, 5, 6, 7, 8, 10, 11, 13]
list.reverse()
print(list) #[13, 11, 10, 8, 7, 6, 5, 5, 4, 3, 2]
print(list.copy()) # [13, 11, 10, 8, 7, 6, 5, 5, 4, 3, 2]
list.clear()
print(list) # []
list = [1,2,3,4,5,5,6,7,8]
print(list[-1]) #8
print(list[:5]) #[1, 2, 3, 4, 5]
print(list[0:]) #[1, 2, 3, 4, 5, 5, 6, 7, 8]
print(list[1:4]) #[2, 3, 4]
print(list.index(2, 0, 5)) #1
print(sum(list)) #41
print(min(list)) #1
print(max(list)) #8
print(all(list)) #true
print(any(list)) #true

#List Comprehension
matrix = [[1,2,3],[4,5,6],[7,8,9]]
data = [row[0] for row in matrix]
print(data) # [1, 4, 7]
