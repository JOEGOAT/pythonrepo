#.Break,continue and pass
#The break and continue are used to handle the flow of a while or a for loop in a python program, meaning the programmer 
# can interrupt or restart the execution of aloop structure, in certain condition

#lets start with break statement
# 1.break -> is used to dertemine the loop in which it resides
# lets see how break works

for number in range(10):
    if number == 7:
        break
    print(number)

list1 = [4,5,6]
list2 = [10,20,30]

for x in list1:
    for y in list2:
        if y == 20:
            break
        print(x*y)
    print("Outside the nested loop")

#2.when python stumbles upon a continue statement inside a for or while loop it ignores the rest of the code below , 
# for the current iteration goes up to the top of the loop and immediately starts the next iteration

list1 = [4,5,6]
list2 = [10,20,30]

for x in list1:
    for y in list2:
        if y == 20:
            continue
        print(x*y)
    print("Outside the nested loop")

#3.pass ->pass is the quivalent of "do nothing". It is just actually a placeholder for whenever you want to leave the addition
# of a piece of code for later and move on to write other segments of your program
#it helps us to keep the syntax of our program valid and not get an error returned when running the program
for x in range (10):
    pass 
print("python") 