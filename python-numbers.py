num1 = 10
num2 = 2.5

#check the type of our variables
print(type(num1))
print(type(num2))

#1.numerical operators
#operation
#Addition 1+2
print(1+2)
#subtraction 2-1
print(2-1)
#Division 5/2
print(5/2)
#Integer division 5//2
print(5//2)
#Multiplication 4*2
print(4*2)
#Raising to a power 4**2
print(4**2)
#Modulo(means finding out the remainder after the division of one number by another)5%2
print(5%2)

#2.comparison operators
#less than <
print(5<2)
#greater than >
print(5>2)
#less than or equal to <=
print(5<=2)
#greater than or equal to >=
print(5>=2)
#equals ==
print(5==2)
#not equals !=
print(5!=2)

#type conversion -> the int( function willl round )
print(int(1.7))
print(float(2))

print(abs(5))
print(abs(-10))

# max(
# min())

#raising to apowe this time using python function
print(pow(5,2)) # where 5 is base and 2 the exponet

first_name="paul"
age=19
print("Hello " + first_name + " you have lived for" + str(age*31536000 ) + "seconds equivalent to "  + str(age) + "years")

#prompt/convert their age in seconds
user_name = input("Please enter your name:")
user_age  = int("input(Enter your age too:")

#calculate /convert their age in seconds
age_in_seconds =user_age * 365.25 * 24 * 60 * 60

#print out the user info in anice format
print("Hello {user_name}, you are {user_age} years old and you have lived for {age_in_seconds} seconds.")

