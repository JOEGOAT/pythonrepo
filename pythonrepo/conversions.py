#Conversions btwn data types
#Means converting frm one data type e.g number to string, there are specific functions which accomplish this.

#Conveting an integer or floating-point number to string using str() method
num =2
f=2.5

print(type(num))
print(type(f))

#convert a no. to a string
num2 = str(num)
print(num2,type(num2))

f2 = str(f)
print(f2,type(f2))

#Convert a string into an integer, using int()
str1 =5
print(type(str1))
int1 = int(str1)
print(int1,type(int1))

#convering integers into floating point no. using float()
num2 = 2
print(type(num2))
f3 =float(num2)
print(f3,type(f3))

f4=22.99
int2=int(f4) 
print(int2,type(int2))

#Moving onto sequences,we can convert a tuple into a list,using list()
tup1=(1,2,3)
print(type(tup1))
list1 = list(tup1)
print(list1, type(list1))

# We can also convert a list to a tuple
list1 = [1, 2, 3]
tup2 = tuple(list1)
print(tup2)

# We can convert a list into a set by using the set() function
set1 = set(list1)
print(set1)

# Lets see how to convert between different numerical representations of numbers i.e decimal, binary and hex notations (base-10, base-2, and base-16)

# convert to binary
num = 10
num_bin = bin(num)
print(num_bin) # 0b1010

# convert to Hex
num = 10
num_hex = hex(num)
print(num_hex) # 0xa

# convert to Binary and Hex, to decimal notation -> use int() function
bin_to_num = int(num_bin, 2)
print(bin_to_num)

hex_to_num = int(num_hex, 16)
print(hex_to_num)

#write a python program that calculates the liquid volume in a sphere, where r = 10
r=10
pie=22/7
h=2
volume=((4*pie*r**3)/3) - (pie*h**2*(3*r-h)/3)
print("volume of the sphere= "+str(volume))
#you can then test the soulution with h = 2 and you should get 
#volume = 4071.5040790523717

# Write a python program that calculates the acceleration given initial velocity v1, final velocity v2, start time t1 and end time t2.
# Test your program with values 0,10,0 and 20 for v1, v2, t1, t2 respectively.
v1=0
v2=10
t1=0
t2=20
acceleration=(v2-v1)/(t2-t1)
print(f"The acceleration of the body is: {acceleration}m/s\u00b2")