#Booleans - lopgical Operators
#Lets evaluate some basic expressions

print(1 == 1)#returns True
print(1 ==2) #returns False

print("Python" == "python")#return False
print(type("Python") == type("python")) #return True
print(3 <= 4) #return True

#there are three main boolean operations and ,or and not
#1.and
a= (1 == 2)
b= (2 == 3)

print(a and b) #returns False
#2.or 

#3.not
print(not(1 == 1))

#log in application
#database values
#username_db = "paul"
#password_db = "password"

#user credentials -> from user
#userName = "munene"
#password = "password"

#log in the user
#if userName == username_db and password == password_db:
#print("Logged in Successfully")
#else:
#raise an error
#print("Invalid username or password")

#bool(function)
#lets use bool() to check the always False values
print("===================")
print(bool(None))
print(bool(0))
print(bool(0.0))

#lets use bool() to check the always True values
print("======================")
print(bool(1.1))
print(bool("Hello"))
print(bool([]))