#create our first empty list -> in order to have an empty list you just have to type the squar brackets and thats it
list1 = [] 

#to check that this is indeed alist , use the old type() function
print(type(list1)) #returns class list

#lets add items to our empty lis1
list1 = ["Cisco", "Juniper", "Avaya",10 ,10.5,-11]

 #lets remmember the len() from strings and use it on our list
print(len(list1))
      
#lets see how we can access elements inside a list.wee the same way as we did with characters in a string ,using indexes

#access the first element in our list
print(list1[0])
print(list1[2])

print(list1[-2])
print(list1[-1])

#As with strings if you enter an invalid index we will get an "index error" in return, stating that list inde4x is out of range
#print(list1[100])

#to check that list are mutable, lets replace an element in the list1 -> we just have to use the = sign to modify this
list1[2] = "HP"
print(list1)

# To update alist , just type in the name of the varible, the variable ponting to the list and in between the square brackets, you have to insert the index
# at which you want the replacement to be made, finally, following the equal sign, just enter the new element an thats it

list2 = [-11, 2, 12]
#max value
print(max(list2))
#min value
print(min(list2))
list3=["a", "b","c"]
print(max(list3))

#print(max("a", "B", 100, -2)) ->returns an error

#how to INSERT using append
list1.append(100)
print(list1)

#ways to remove list elements
#1.del command
del list1[4]

#2.pop method
list1.pop(0)

#3.remove()
list1.remove("HP")

print(list1)

#how to insert an element at a partciluar index in list
#its accomplished by using the insert() method
list1.insert(2,"Nortel")
print(list1)

#appending alist to another list
#accomplished using external() method
list2 = [9,99,999]

list1.extend(list2)
print(list1)


#index of elements
print(list1.index(-11))

#append some values
list1.append(10)
list1.append(10)
list1.append(10)

#count the occurrence of 10
print(list1.count(10))

#lets look at ways of sorting elements
#use sort()
list2.append(1)
list2.append(25)
list2.append(500)

#sort the the list2 in an ascending order
list2.sort()
print(list2)

#reverse or descending order
#we have reverse() method for this
list2.reverse()
print(list2)

#to sort elements of a list and create a new list in memory at the same time you have the sorted() function available
print(sorted(list2))
print(list2)

#for the reverse order you have to addd an argument inside the paranthesess which have the value of true assigned
print(sorted(list2, reverse=True))

#you can use help() to know about a built in function in python
print(help(len))

#you can concatenate or repeat using plus multiplication operators
print(list1 + list2)

#repeating a list
print(list2*5)

list3 = [1,2,3,'a','b','c']
#extract
#1.[1,2,3]
print(list3[0:3])
#2.[1,2,3]
print(list3[:3])
#3.[3,'a','b']
print(list3[2:5])
#4.[1,2,3,'a','b','c']
print(list3[:6])

#use negative indexes to slice the following
#5.[3,'a','b']
print(list3[-4:-1])
#6.['a','b','c']
print(list3[-3:])

#use a step to extract the following
#7.[1,3,'b']
print(list3[::2])
#8.['c','b','a',3'2'1]
print(list3[::-1])


