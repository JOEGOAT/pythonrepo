#an empty dictionary
dict1 = {}
#check the type
print(type(dict1))

#adding data to the dict1
dict1 = {"Vendor":"Cisco","Model": "2600","IOS":"12.4","Ports":"4"}

#each dictionary element consists of akey ,a colon, and a value,followed bya comma
# DICTIONATY METHODS

# first,lets  extract the corresponding value of a specified key only that we dont specify an index,we specify the associated key for the value
# we want to extract

#extract '12.4'
print(dict1["IOS"])
#extract 'Cisco'
print(dict1["Vendor"])

#lets try adding a new key value pair.it is done by simply assigning a new value to the new key
dict1["RAM"] = "128"
print(dict1)

#we can modify the value of a dictinary
dict1.update({"IOS" :"15.8"})
print(dict1)

dict1["IOS"] = "15.8"

#we can also delete a pair from dictionary
del dict1["Ports"]
print(dict1)

# we can use the len() function
print(len(dict1))

#we can verify t=if a certain string is a key in a dictionary or not
print("IOS" in dict1) 
print("ports" in dict1)


#there are three important methods to deal with keys and values in dictionary
#1.keys() ->This method is used to obtain a list having the keys in a dictionary as elements
print(list(dict1.keys()))

#2 valuees()->used to obtain a list having the values in a dictionary as elements
print(list(dict1.values()))

#3. items()->used to return a list of tuples each tuple contains the key and value of each dictionary
print(list(dict1.items()))