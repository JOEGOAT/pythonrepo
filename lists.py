# create our first empty list -> in order to have an empty list you just have to type the square brackets
list1 = []

# to check that this is indeed a list, use the old type() function
print(type(list1)) #returns class list

# let's add items to our empty list1
list1 = ["Cisco", "Juniper", "Avaya", 10,10.5,-11]
# let's remember the len() from strings and use it on our lists
print(len(list1))

#let's see how we can access elements inside a list. Well, the same way as we did with characters in a string,using indexes
# access the first elements in our list
print(list1[0])
print(list1[2])

print(list1[-2])
print(list1[-1])

# As with strings, if we enter an invalid index we will get an "indexerror" in return, stating that the list index is out of range
#print(list1[100])

# To check that lists are mutable,let's replace an element in the list -> we just have to use the equal sign to modify this
list1[2] = "HP"
print(list1)

# To update a list just type in the name of the varuable pointing to the list and in btwn square brackets you have to insert the index at which you want the replacement to be made,Finally, following the equal sign just enter the new element and that's it.

#list methods
#max() and min() functions

#let's consider list2
list2 = [-11,-0,12]
#max value
print(max(list2))
#min value
print(min(list2))

#what about a lists of strings
list3 = ["a","b","c"]
print(max(list3))

#print(max("a","B",100.-2))

#lets check the available list methods we have at hand

# First, we should learn how to append a new element to a list. consider list1
print(list1)

#to append an element to this list, just use the append() method
list1.append(100)
print(list1)

#We have 3 ways for removing lists elements
#1. -> Del command
# del list_name[element_index]
del list1[4]

#2. -> pop() method
#Removes an element by its element
list1.pop(0)

#3. ->Remove()
#Removes an element by specifying the element itself
list1.remove("HP")
print(list1)

#How to insert an element at a particular index in a list
#This is easily accomplished by using the insert() method
list1.insert(2,"Nortel")

#Appending a list to another list
#accomplished using the extend() method
list2 = [9,99,999]

list1.extend(list2)

print(list1)

#count() and index() methods -> slices
#lets find out the index of an element in our list and how to count the occurrences of an elemnt in a list
print(list1.index(-11))

#append some values
list1.append(10)
list1.append(10)
list1.append(10)

#count the occurrence of 10
print(list1.count(10))

#ways of sorting elements in a list
#using sort() methods
#consider list2

list2.append(1)
list2.append(25)
list2.append(300)

print(list2)

#sort the list in an ascending order
list2.sort()

print(list2)

#sort the list in a reverse/descending order
list2.reverse()

print(list2)

#The 2 methods above modifies the list in place,meaning once applied there's no other list created
#To sort elements in a list and create a new list in mem at the same time we use sorted() function
print(sorted(list2))

print(list2)

#If you want to use the same function to reverse the order, just add an argument inside the parenthesis. This argument is called reverse and it must have the value of True assigned to it.
print(sorted(list2,reverse=True))

#print(help(sorted)) -> gives us info on sorted function, can be used for others too
#You can repeat a list using plus and multiplication operators
print(list1 + list2)

#repeating a list
print(list2*5)

#slicing is removing parts of element an leaving the rest intact
#var1[5:10]

list3 = [1,2,3,'a','b','c']

#Use slicing to extract the following
#1. [1,2,3]
print(list3[0:3])

#2. [1,2,3]
print(list3[:3])

#3. [3,'a','b']
print(list3[2:5])

#4. [1,2,3,'a','b','c']
print(list3[:])

#Use negative indexes to slice the following
#5. [3,'a','b']
print(list3[-4:-1])

#6. ['a','b','c']
print(list3[-3:])

#Use a step to extract the following
#7.[1,3,'b']
print(list3[:5:2])
print(list3[::2])

#8.['c','b','a',3,2,1]
print(list3[::-1])
