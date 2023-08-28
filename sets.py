#sets don't allow duplicates
#evidence of this is:
list4 =[1,2,3,4,5,2,3]
print(list4)
print(set(list4))

# NB -> The set element removed duplicate elements in list4, which is a very useful feature to have

#other ways of maki
set1 = set([11,12,13,14,15,15,15,11])
print(set1)
print(type(set1))

#other ways of making a set
#using curly braces
set2 ={11,12,13,14,15,15,15,11}
print(set2)
print(type(set2))

#We can find out no. of elements by using len() function
print(len(set2))

#We can check if element is/isn't member of a set by using 'in' and 'not in' keywords
print(11 in set2)
print(10 in set2)
print(10 not in set2)

# Sets are mutable, so we can add/remove elements frma a set in the following manner
set2.add(16)

print(set2)

#Set Method and Operations
set1 = {1,2,3,4}
set2 = {3,5,8}

#to identify common elements using intersection()
print(set1.intersection(set2))
print(set2.intersection(set1))

#Let's see which elements are in set1 and not in set2 using defference() method
print(set1.difference(set2))

#You can remove a random element in set using pop() method
print(set.pop())
print(set1)

#we can clear a set using clear()
set1.clear()
print(set1)