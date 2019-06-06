#data structures of Python

#Lists
print("*****LISTS*****")
colors = ["red", "blue", "green", "yellow", "black"]
print(colors)
l1 = [1, 2, 3, (6, 7, "fghfg")]
print(l1)

#List access
print(colors[4])#index
print(colors[-3])#negative index

#List slices
print(colors[2:4])#index 2 to 3, last element excluded
print(colors[2:])#index 2 to end
print(colors[:-2])#index 0 to -3, element at index -2 excluded

#Setting slice of list
colors[2:4] = [1, 2]
print(colors)

#Combining lists
list1 = [1, 2, 3, 4]
list2 = [8, 7, 6, 5]
list3 = list1 + list2
print(list3)

#Deleting an item
del colors[3]
print(colors)

#Deleting items
del list3[2:5]
print(list3)

#Removing an item
list3.append(6)
list3.remove(6)
print(list3)

#Popping an item
item = list3.pop(2)
print(item)

#Sorting a list
list3.sort()
print(list3)

#Reversing a list
list3.reverse()
print(list3)

#Counting number of instances of parameter in a list
count = list3.count(3)
print(count)

#Checking if value is in a list
isIn = 4 in list3
print(isIn)

#Copying a list
list4 = list3.copy()
list4.clear()
print(list3 + list4)

#Tuples
print("*****TUPLES*****")
tuple1 = (1, 2, 3, 4, 5)
print(tuple1)
tuple2 = 5.5, 4, "hey", 'r'
print(tuple2)
tuple3 = (2, 3, ["fgdf", 5.567], 3456)
print(tuple3)

#Tuple methods
i = tuple2.index(4)
print(i)

i = tuple2.count("hey")
print(i)

print("*****LISTS AND TUPLES*****")
#List to tuple
list1 = [1, 2, 3, 4]
newTuple = tuple(list1)
print(newTuple)

#Tuple to list
tuple1 = (5, 6, 7, 8)
newList = list(tuple1)
print(newList)

#Compare function
t1 = (1, 2, 3, 4.324)
l1 = [5, 6, 7, 8.1]
print(max(t1))
print(max(l1))

#Dictionaries
print("*****DICTIONARIES*****")
dict1 = {1:'r', 2:'e', 3:"Hello", 5:28}
print(dict1)

#Dict access
print(dict1[3])#getting value mapped to key
print(dict1.get(265))

#Dict updating
dict1[1] = 34 #changing a value
print(dict1)
dict1[4] = "sup" #adding a value
print(dict1)
