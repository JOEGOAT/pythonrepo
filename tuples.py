my_tuple = ()
print(type(my_tuple))
#to create tuple with single element you have to write a comma after it
my_tuple = (9)
print(type(my_tuple))

my_tuple = (9,)
print(type(my_tuple))

#lets populate our tuple
my_tuple = (1,2,3,4,5)
print(my_tuple[0])
print(my_tuple[1])
print(my_tuple[-1])
print(my_tuple[-2])

#since they are immutable you cannot add, modify
#my-tuple[1] = 10 -> returns a type error since it doesnot support

#you cannot remove elements
# del my_tuple[1] -> returns type error

#tuple assignment
tuple1 = ("Cisco","2600", "12.5")
(vendor,model,ios) = tuple1
print(vendor)
print(model)
print(ios)

# This is also called tuple packing and unpacking and you can see it as a kind of mappping between elements of diffrent tuples 

#An important thing to remember here is both tuples should have the same numbers of elements otherwise if you have 
# diffrent number of elements ,a value erroe will be returned


tuple2 = (1,2,3,4)
# (x,y,z) = tuple2

#You asign values in a turple
(a,b,c) = (10,20,30)
print(a)
print(b)
print(c)

#tuple methods
# as with strings and lists ,we can perform some basic operations on tuples
# 1.len()
print(len(tuple2))

#we have the min(), max()
print(min(tuple2))
print(max(tuple2))

#we can also concatenate and multiply
print(tuple2 + (5,6,7))

print(tuple2 * 3)

#slicing of tuples
#1.(1,2)
print(tuple2[0:2])
# 2.(1,2)
print(tuple2[ :2])
# 3.(2,3,4)
print(tuple2[1:])
# 4.(1,2,3,4)
print(tuple2[:])

#negative
# 1.(1,2)
print(tuple2[-4:-2])
# 2.(3,4)
print(tuple2[-2:])
# 3.(4,3,2,1)
print(tuple2[::-1])
# 4.(1,3)
print(tuple2[::2])

#you can check if an element is a member of a tuple or not using in and not in
print(3 in tuple2)
print(3 not in tuple2)
print(5 not in tuple2)

#we cann use del to delete the entire tuple
del.
print(tuple2)

