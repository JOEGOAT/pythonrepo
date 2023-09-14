#Functions

#a function is a block of code that performs a specific task when called /invoked
#for a function to execute it must be invoked or called 
#To call a function you simply type the name of function followed bt panthesis outside the function

#syntax
# def function_name():
    #code to execute goes here

#our first function that greets everyone
def greet_everyone():
    print("Hello everyone!!")
#greet_everyone()

#why use functions?
#functions allow code managebality
#allow code reusability
#reduces code repetition

# a function that adds 2 numbers together
def my_function():
    sum = 3+1
    print(sum)
# my_function()
# my_function()
# my_function()
# my_function()

#Parameters and Arguments

#Parameters
#its a value passed to the paranthesis of a function definition ->(variable(s))
#information passed into a function

#Arguments
#its is a value to the paranthesis of a function call

def greet_user(user_name):
    print(f"Hello, {user_name}")
    
#greet_user("Munene")

#a function that takes in 3 numbers as params and displays their sum
def add(a,b,c):
    print(a+b+c)
#add(10,15,37)
#add(20,15,37)
#add(10,165,37)
#add(10,165,347)

#return keyword
#used to terminate a function and then return a value
def productoftwoNums(a,b):
    return a*b
product = productoftwoNums(3,4)
print(product + 38)

#print(productoftwoNums(4,4))

#write a python program that has five function where the first one returns the name of the user ,second returns the age of user, third returns the age in seconds that the user has lived , fourth returns the decades and the fifth prints/returns the user information ina very nice format

def username():
    name = input("Please enter your name: ")
    return name

def user_age():
    age = input("Please enter your age too: ")
    return int(age)

def user_age_in_seconds(age):
    return age * 365.25*24*60*60

def decades_lived(age):
    return age//10

def display_user_info():
    userName = username()
    userAge = user_age()
    ageinseconds = user_age_in_seconds(userAge)
    decades = decades_lived(userAge)

    print(f"Hello {userName}, You have lived for {decades} decades, {ageinseconds} seconds, which means you are {userAge} years old.")

#display_user_info()



# def smallest_odd_integer(numbers):
#     odd_numbers = []
#     for number in numbers:
#         if number % 2 == 1:
#             odd_numbers.append(number)
#     return min(odd_numbers)



def smallest_odd_integer(numbers):
    odd_numbers = []
    for number in numbers:
        if number % 2 == 1:
            odd_numbers.append(number)
    #return min(odd_numbers)
    odd_numbers.sort() 
    smallest_odd = odd_numbers[0]
    return smallest_odd

my_list =[23,23,544,234,56,43,34,3,2]
print(smallest_odd_integer(my_list))


#write a python program that takes 3 integers compares them and returns the smallest among them
def smallest(a,b,c):
    integers =[a,b,c]
    integers.sort()
    smallest = integers[0]
    return smallest
print(f"The samllest number is: {smallest(34,1,10)}")

#or
def smallest (num1,num2,num3):
    if num1 <= num2 and num1 <= num3:
        return num1
    elif num2 <= num1 and num2 <= num3:
        return num2
    else:
        return num3 

print(f"The samllest number is: {smallest(34,4,10)}")        

#or
def smallest (num1,num2,num3):
    small_num = 0
    if num1 <= num2 and num1 <= num3:
        small_num = num1
    elif num2 <= num1 and num2 <= num3:
        small_num = num2
    else:
        small_num =  num3 

    return small_num

print(f"The samllest number is: {smallest(34,4,10)}")      

