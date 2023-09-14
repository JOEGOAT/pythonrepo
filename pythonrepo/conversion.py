#lets try to convert an integer or floating point number to string using str() method

num = 2
f = 2.5

print(type(num))
print(type(f))

#convert a number to a string
num2 = str(num)
print(num2, type(num2))

f2 = str(f)
print(f2, type(f2))

#lets try this backwards and convert a string into an integer ,using int() function
str1 = 5
print(type(str1))
int1 = int(str1)
print(int1, type(int1))

#You can also convert integers into floating-point numbers, using float() function and vice versa
num2 = 2
print(type(num2))
f3 = float(num2)
print(f3, type(f3))

f4 = 22.99
int2 = int(f4)
print(int2, type(int2))

# moving on to sequences , lets convert a tuple into a list using list() function
#tup1 = (1,2,3)#

#convert to binary
num = 10
num_bin = bin(num)
print(num_bin) #0b1010

#convert to hex
num = 10
num_hex = hex(num)
print(num_hex) #0xa

#convert to binary and hex, to decimal notation ->use int()
bin_to_num = int(num_bin,2)
print(bin_to_num)

hex_to_num = int(num_hex,16)
print(hex_to_num)
