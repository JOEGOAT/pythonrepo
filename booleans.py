# Booleans - logical Operators
# Let's evaluate some basic expressions

print(1 == 1) #returns True
print(1 == 2) #returns False

print("Python" == "python") #return False
print(type ("Python") == type("python")) #return True
print(3 <= 4) #return True

# There are 3 main boolean Operations, each of them having a specific operator namely: "and", "or" and "not"
#1. and -> means both operands should be True, in order to have the entire expression evaluated as True.
a = (1 ==2)
b = (2 ==3)

print(a and b) #returns False

#2. or -> if at least one of the expressions evaluates to True, then the Final result is True, if they are both false then the final result will be false as well.
#when using "or" it's enough if only one expression is true in order to have true as the final result

#3. Not -> means simply denying an expression.
print(not(1 ==1)) #returns False

#log in application

#database values
username_db = "dennis"
password_db = "password"

#user credentials -> frm the user
userName = "Dennis"
password = "password"

#log if the user
if userName == username_db and password ==password_db:
    #if username mached ... log in the user
    print("Logged in Successfully")

else:
    print("Invalid Username or Password...")

#bool () function -> helps as evaluate expressuins as true or false
#using bool to check if values are always flase
print("==================")

print(bool(None))
print(bool(0))
print(bool(0.0))

#using bool to check if values are always true
print("===============")

print(bool(1))
print(bool(1.1))
print(bool("Hello"))
print(bool([]))