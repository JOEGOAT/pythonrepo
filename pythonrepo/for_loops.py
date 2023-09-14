vendors = ["Cisco","HP","Nortel","Avaya","Juniper"]
#Let's see how we can work with a for loop
for each_vendor in vendors:
    print(each_vendor)

my_string = "Cisco"

for letter in my_string:
    print(letter)
    print(letter*2)
    print(letter*3)

#Consider a range that starts frm 0 and going upto, but not including 10, with the default step of 1.That would return the integers 0 all the way to 9 in ascending order

r = range(10)
for numbers in r:
    print(numbers*2)

#Let's see a more common use of range() function inside a for statement.
#What if we want to iterate over a list using list indexes?
#What do i mean?
#We still have the vendors list in memory
print(vendors)
#Remember the len() function frm earlier
print(len(vendors))

# We know that range(5) returns integers frm 0 to 4 but not including 5. We can convert this range into a list, using list() function. let'do it
print(list(range(5)))

# We can look at the elements of this list as being the indexes of each element of our list,vendors. So, the element "Cisco" would be positioned at index 0, "HP" at index 1 and so on.

#This means if we want to get a list of indexes to iterate over, using a for loop, we can use this range(len(vendors)) to obtain that list
print(list(range(len(vendors))))

for element_index in list(range(len(vendors))):
    print(vendors[element_index])

#What we did there is we passed the result of one function, len(), to another function, range()
#The result is a range, consisting of all the indexes in the vendors list. We then assign each index in this range to the element_index temporary varaible and executed a piece of code for each index.
#In translation, we told python to check the vendors list, then create a range using that length as an argument for the range() function.
#Finally, python prints out each element by its index - vendors[0], vendors[1] and so on until the list is exhausted

#Another very useful way to iterate over a sequence is by using both the index and the element value as iterating variables.This can be achieved using the enumerate() function in Python.
for index,element in enumerate(vendors,):
    #print(index,element) -> output with no dot after the integer
    #or to add a dot after the integer we:
    print(f"{index +1}.{element}")

    #or use "start=" to begin with 1