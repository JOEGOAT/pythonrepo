#nest if statements

string1 = "Cisco"

if "i" in string1:
    if len(string1) > 4:
        if type(string1) == str:
            print(string1,len(string1),type(string1))

#you can express the above program like this
if "i" in string1 and len(string1)>4 and type(string1) == str:
    print(string1,len(string1),type(string1))

integer = int(input("Hello user enter an integer: "))

if type(integer) is int:
    if integer >10:
        print("User you number is an integer and greater than 10")
    elif integer <10:
        print("User you number is an integer but less than 10")
    elif integer is 10:
        print("User you number is an integer but equal to 10")


#nested for loop
#lets assume that we have two lists and we want to multiply each element of the first list by each element of the second.
#for this we iterate over both lists at the same time take each element into account,do the multiplication and return results

list1 = [4,5,6]
list2 = [10,20,30]
        
for x in list1:
    for y in list2:
        print(x*y)   
# print(x)