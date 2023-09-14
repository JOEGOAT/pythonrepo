vendors = ["Cisco", "HP","Nortel", "Avaya","Juniper"]
#lets see how can work with a for loop

for each_vendor in vendors:
    print(each_vendor)

my_string = "Cisco"
for letter in my_string:
    print (letter)
    print (letter*2)
    print (letter*3)

# consider a range that start from 0 and going upto, but not including 10, with the default step of 1 .That would return 
# the intergers 0 all the way to 9 in ascending order

r = range(10)
for numbers in r:
    print(numbers*2)
    
#lets see a more common use of the range () function inside a for statement
#what if we want to iterate over a list using list indexes
#what does that mean?
#we still have the vendors list in memory..
print(vendors)

#rememebr the len() function from earlier? lets apply it to our list
print(len(vendors))
#we know that range of 5 returns the integers starting with 0 up to but not including 5.Moreover we can convert this
# range into a list, using the list() function.lets do this
print(list(range(5)))

#we can look at the elements of this list as being the indexes of each element of our list,vendors.So the element"Cisco"
# would be positioned at index o,"HP" at index 1 and so on
#This means that if we want to get a list of indexes to iterate over,using a for loop,we can use range(len(vendors)) to 
# obtain that list 
print(list(range(len(vendors))))

for element_index in (list(range(len(vendors)))):
    print(vendors[element_index])


#what we have done above is we passed the result of one function len(), to another function, range()
#The result is a range, consisting of all the indexes in the vendors list .
#we then assigned each index in this range to the element_index temporary variable and executed a piece of code for each
# index.
# In translation we told python to check the length of th vendors list, then create a range using that length as an 
# argument for the range() function
# Finally, Python prints out each element by its index - vendors[0], vendors [1] and so on until the list is exhausted 
 
#Another very useful way to iterate over a sequence is by using both the index and the element value as iterating variables
# This can be achieved using the enumerate () function in Python  

for index, element in enumerate(vendors):#you can put a comma after vendors and say start=1 to make the list start from 1
    #print(index, element)
    print(f"{index +1}. {element}")


