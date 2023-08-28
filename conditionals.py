#if syntax
#if condition:
#    code(s) to execute if condition is true

x=4

if x>5:
    print("x is greater than 5")
    print(x*2)

# Our if block doesn't return anything, comma since 4 isn't greater than 5 and the expression is evaluated as false, bottomline, if python evaluates the expression as true, it will execute the indented code below the if statement, otherwise it will skip it and move on to the rest of the code if any.


#Else
#What if you want to handle multiple cases?
#let's say you want smth to be printed out, regardless of the true or false result of the evaluation.For this you will use the 'elif' or 'else' statements

x=4

if x>5:
    print("x is greater than 5")
else:
    print("x is not greater than 5")

#Else statement is used to cover all other statements not covered by the if statement above it.
#If the expression following the if keyword is true, the indented code below it will be executed. 
# Otherwise, if the expression is evaluated as false the indented code below else gets executed


#What if we want to be more granular and specify more cases and possible outputs in our program?
#We use an elif statement

#Let's say we want to print "x is greater than 5" if indeed x is greater than 5, "x is equal to 5" incase x is equal to 5 then "x is less than 5" for all other cases.
#We should then ass the elif statements in btwn if and else
#Else statement should always be last in an if/elif/else block

x=4

if x>5:
    print("x is greater than 5")
elif x==5:
    print("x is equal to 5")
else:
    print("x is less than 5")


#Asks user for the temperature
temp = float(input("Enter the current temperature in degree celcius: \u00b0"))

if temp>23:
    print("Cover your tomatoes")
elif temp==23:

    print("Enjoy your fruit")
else:
    print("Uncover your fruit")

