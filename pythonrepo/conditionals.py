#python conditionals->if / for / while

#if syntax
# if condition :
#     codes to execute if condition is true

x = 10
if x > 5:
    print("x is greater than 5")

#Else
x = 4
if x > 5:
    print("x is greater than 5")
else:
    print("x is not greater than 5")

#lets say we want to print "x is greater than 5" if indeed x is greater than 5 , "x is equal to 5" in case x will become
#  equal to 5 at some point and "x is less than 5" for all other cases . we should then add the elif statement in between
#  if and else

#the else statement should always be the last statement in an if/elif/else block

x = 5
if x > 5:
    print("x is greater than 5")
elif x==5:
    print("x is equal to 5")
else:
    print("x is less than 5")
