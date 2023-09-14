#there are 2 ways of creating sets
#1.using the set() function

#to prove that sets dont have duplicates like lists
list4 =[1,2,3,4,5,2,3]
print(list4)
print(set(list4))
#set() function removes duplicates in list4
#you can also create a set by passsing a raw sequenceto set () function like a string
set1=set([11,12,13,14,15,15,15,11])
print(set1)
print(type(set1))

#2.creating a set using curly braces.It is available for python versions starting with 2.7
set2 = {11,12,13,14,15,15,15,11}
print(set2)
print(type(set2))

#we can also find out number of elements in a set using len()
print(len(set2))

#we can also check if an element is or not a amember of aset by using 'in' and 'not in' key words
print(11 in set2)
print(11 not in set2)
print(10 not in set2)

#sets are mutable so we can add or remove elements
set2.add(16)
set2.add(16)
print(set2)

#To better understand set methods and operation
set1 = {1,2,3,4}
set2 = {3,5,8}

#to identify common elements using intersection ()
print(set1.intersection(set2))
print(set2.intersection(set1))

#Lets see which elements are in set 1 and not in set2 using difference () method
print(set1.difference(set2))

#'to unify sets use unio() but common element will not be duplicated
print(set1.union(set2))

#You can remove a random element in set using pop() method
print(set1.pop())
print(set1)

#we can clear a sey using clear()
set1.clear()
print(set1)

#we can modify the value in dictionary
