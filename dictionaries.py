#let's create an empty dictionary
dict1 ={}

#check the type
print(type(dict1))

#let's add some data to our dictionary
dict1 = {"Vendor":"Cisco","Model":"2600","IOS":"12.4","Ports":"4"}
d1 = {1:"First Element", 2:"Second Element"}
# Each dictionary element consists of a key,a colon and a value, followed by a comma

#Dictionary methods
#Consider dict1
#First, let's extract the corresponding value of a specified key.This can be done similarly to acccessing elements inside a list only that we don't specify an index,we specify the associated key for the value we want to extract.

#extract '12.4'
print(dict1["IOS"])

#extract 'Cisco'
print(dict1["Vendor"])

#Let's add a new key-value pair.This is done by simply assigning a new value to the new key

#dict1.update({"RAM":"128"})
dict1["RAM"] = "128"
print(dict1)

#we can modify the value of a dictionary

#dict1.update({"IOS":"15.8"})

#another way
dict1["IOS"] = "15.8"
print(dict1)

#We can also delete a pair frm a dictionary, using the del command
del dict1["Ports"]
print(dict1)

#We can use the len() function to find out the number of elements ina dictionary
print(len(dict1))

#We can verify t=if a certain string is a key in a dictionary or not
print("IOS" in dict1)
print("Ports" in dict1)

#There are 3 important methods to deal with keys and values in directory
#1. Keys() ->This method is used to obtain a list having the keys in a dictionary as elements.
print(list(dict1.keys()))

#2. Values() -> This method is used to obtain a list having the values in a dictionary as elements.
print(list(dict1.values()))

#3. Items() -> This method returns a list of tuples, each tuple containing the key and the value of each dictionary pair.
print(list(dict1.items()))

#1. ->Create a dictionary of keys a, b and c where each key has as values a list frm 1-10, 11-20 and 21-30 respectively. then print out the dictionary in a nice formart.

#One way
A = list(range(1,11))
B = list(range(11,21))
C = list(range(21,31))

print({'a':A, 'b':B, 'c':C})

#Second way
dict2 = dict(a =list(range(1,11)),b=list(range(11,21)),c =list(range(21,31)))
print(dict2)

#3rd way
dict3  ={'a':list(range(11)),'b':list(range(11,21)),'c':list(range(21,31))}
print(dict3)

#2. ->Access the 3rd vakue of key b  frm the directory
#Expected output :13
v =dict1["b"][2]
print(v)
v=dict2["b"][2]
print(v)
v=dict3["b"][2]
print(v)