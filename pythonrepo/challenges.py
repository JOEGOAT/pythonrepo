#first_name="paul"
#age=19
#print("Hello " + first_name + " you have lived for" + str(age*31536000 ) + "seconds equivalent to "  + str(age) + "years")

#1.prompt/convert their age in seconds
#user_name = input("Please enter your name:")
#user_age  = int(input("Enter you age too:"))

#calculate /convert their age in seconds
#age_in_seconds =user_age * 365.25 * 24 * 60 * 60

#print out the user info in anice format
#print(f"Hello {user_name}, you are {user_age} years old and you have lived for {age_in_seconds} seconds.")

#2.Pythogras theorem
#side_A = int(input("enter size of side_A of a right angled triangle"))
#side_B = int(input("enter size of side_B of a right angled triangle"))

#Hypotenuse = round(side_A**2 + side_B**2,4)

#print(f"The Hypotenuse of a right angled triangle with {side_A} cm and {side_B} cm is {Hypotenuse} cm\ub002")

#3.write a python program that prompts the user to enter their weight in kgs and height in meters then computes their BMI(body masss index)

#weight = float(input("enter your weight in kgs"))
#height = float(input("enter your height in meters"))

#BMI2 = weight/height**2
#compute the BMI
#BMI = round (weight/height**2,4)

#print(f"your BMI is{BMI} kg/m\ub002")
#print(f"Your BMI2 is :{BMI2:.2f} kg/m\ub002")


#4 write a python program that gets the radius of a circle in cm from the user.The program then returns the area and perimeter of that circle.
#prompt user for radius
#radius = float(input("please enter the radius of the circle in cm  "))

#compute the area and perimeter
#area = round((22/7) * (radius**2),4)
#perimeter = round((22/7) * (radius*2),4)

#output the perimeter and area
#print(f"The area is {area} cm\u00b2")
#print(f"The perimeter is {perimeter} cm")

#5.write a python program that prompts the user to enter marks for 5 subject and then computes the average score.
#The program should print the name and average score in a nice format
#prompt the user for their names
#user_name = input("Please enter your Name: ")

#prompt the user for the scores of the subjects
#sub1 = float(input("Enter marks for subject a "))
#sub2 = float(input("Enter marks for subject b "))
#sub3 = float(input("Enter marks for subject c "))
#sub4 = float(input("Enter marks for subject d "))
#sub5 = float(input("Enter marks for subject e "))

#add all the subjects
#total_score = sub1 + sub2 + sub3 +sub4 + sub5
#calculate the average score
#average_score = total_score/5

#output the users info
#print(f"Hello {user_name},your score is {average_score}%. ")

#6 write a python program that asks a user for the names of 5 students stores them in alist ,the program should then ask the user for
#the user for the index of a user and then display that student alongside the index
#solution 1

#students_names = input("Please enter the names of 5 students with no spaces separated with comma: ")
#students_list = students_names.split(",")
#print(students_list)

#another way
#stud1 = input("Enter the name of the first student")
#stud2 = input("Enter the name of the second student")
#stud3 = input("Enter the name of the third student")
#stud4 = input("Enter the name of the four student")
#stud5 = input("Enter the name of the five student")

#students = [stud1,stud2,stud3,stud4,stud5]

#create an empty list
#students = []

#append the names to the list
#students.append(stud1)
#students.append(stud2)
#students.append(stud3)
#students.append(stud4)
#students.append(stud5)
#print(students)

#another way
#stud1 = input("Enter the name of the first student: ")
#stud2 = input("Enter the name of the second student: ")
#stud3 = input("Enter the name of the third student: ")
#stud4 = input("Enter the name of the four student: ")
#stud5 = input("Enter the name of the five student: ")

#create a list
#students = [stud1,stud2,stud3,stud4,stud5]
#print(students)

#ask the user for an index
#student_index = int(input("Enter an index between 1 and 5, to display a student: "))

#get the student from the list
#student_name = students[student_index -1]

#display the student name with their index
#print(f"{student_name} is at index: {student_index}")

#7.write a python program that asks the user for their age and then output the decades the user has lived i.e 18 -> 1 decade(i decade = 10 years)
#user_age = int(input("Please enter your age in years here: "))
#age_in_decades = user_age // 10 # you put two slashes in order not to get a reminder
#print(f"Hello user you have lived for {age_in_decades} decades.")

# 8.create a dictionary of keys a,b and c where each key has a value a list from 1-10, 11-20, and 21-30 respectively.Then print out the dictionary
# in a nice format

#a = list(range(11))
#b = list(range(11,21))
#c = list(range(21,31))

#dict1 = {"a":a, "b":b,"c":c}
#print(dict1)

#another way
#dict2 = dict(a = list(range(11)) ,b = list(range(11,21)) ,c = list(range(21,31)) )
#print(dict2)

#another way
#dict3 = {'a' : list(range(11)),'b':list(range(11,21)),'c' : list(range(21,31)) }
#print(dict3)

#b.access the third value of key b from the dictionary
#expected output :13
#v = dict1["b"][2]
#print(v)
#v = dict2["b"][2]
#print(v)
#v = dict3["b"][2]
#print(v)

#9.Write a python program that calculates the liquid volume in a sphere ,where r is always 10
#you can test the solution withy h =2 and you should get 
#volume = 4071.504079052317

#solution

#pi = 22/7
#r = 10
#h = 2

#volume = ((4* pi * r**3) /3) -(pi * h **2 *(3*r - h) /3) 
#print(volume) 

#10.write a python program that calculates the acceleration given initial velocity v1, final velocity v2,
# start time t1, and the end time t2.
#test your program with values 0,10,0 and 20 for v1,v2,t1 and t2 respectively
#expected output :o.5

#t1 = 0
#t2 = 20
#v1 = 0
#v2 = 10
#acceleration  = (v2-v1) / (t2-t1) 
#print(f"The acceleration of the body is: {acceleration} m/s\u00b2")


#11.write a python program that asks a user for temperature and
# returns if temperature is above 23 to cover the tomatoes and if below 23 to uncover and once its 23 enjoy the fruit

#temp = float(input("Please enter the temperature here in degree celcius: "))

# #if temp > 23.0:
#     print("Please cover your tomatoes the tempereature is high")
# elif temp == 23:
#     print("You can enjoy your tomatoes")    
# else:
#     print("uncover your tomatoes its good temperature" )

# 12.write a python program that asks the user for their name and for scores for 5 units then stores them in a list/tuple/set/dictionary.
# Then calculates the average mark of the student.The program then grades the student based on the average mark.
# use the following range table to grade the student
#range          grade
#80 - 100       A
#70 - 79        B
#60 - 69        C
#50 - 59        D
# 0 - 49        F
# print("\t\t\tCPL GRADING SYSTYM")
# print("==="*20)

# stud_name = input("Please enter your name here: ")
# print ("===" *20)

# math = float(input("Enter marks for subject math "))
# english = float(input("Enter marks for subject english "))
# kiswahili = float(input("Enter marks for subject kiswahili "))
# biology = float(input("Enter marks for subject biology "))
# chemistry = float(input("Enter marks for subject chemistry "))

# #there is some problem here you can enter more than 
# print ("===" *20)
# #storing them in a list
# subject_scores = [math,english,kiswahili,biology,chemistry]
# print(subject_scores)
 

# #add all the subjects
# total_score = sum(subject_scores)
# #calculate the average score
# average_score =sum(subject_scores)/len(subject_scores)
# print(average_score) 
 
# grade = ""

# if average_score >= 80 and average_score <= 100:
#     grade = "A"
# elif average_score >= 70 and average_score <=79:
#     grade ="B" 
# elif average_score >= 60 and average_score <=69:
#     grade ="C" 
# elif average_score >= 50 and average_score <=59:
#     grade ="D"
# elif average_score >=0 and average_score <=49:
#     grade ="F"

# #OUTPUT THE TOTAL SCORE
# #print(grade)

# #output the student info
# if average_score>100:
#      print("Invalid score,Please enter valid marks!!!")
# else:
#     print(f"Hello {stud_name}, You have scored {average_score}%, which is Grade: {grade}")

# print ("===" *20)

#13.times table
#for x in range(1,13):
#    print(f"{10} X {x} = {x * 10}")

# get the times table from user
#times = int(input("Please enter the times table: "))
#for x in range(1,13):
#    print(f"{times} X {x} = {x * times}")

# 14 create a python dictionary that has keys a,b and c where each key has as values list of intergers 1-10, 11-20 and 21-30
# respectively
# make program produce the following
# a has[1,2,3,4,5,6,7,8,9,10] 
# b has[11,12,13,14,15,16,17,18,19,20]
# c has[21,22,23,24,25,26,27,28,29,30]

# dict1={
#     'a': list(range(1,11)),
#     'b': list(range(11,21)),
#     'c':list(range(21,31))
# }
# for key, value in dict1.items():
#     print(f"{key} has value {value}")

#15. create a times table from 1-12
#hint nested for loop
times = int(input("Enter the number: "))
for a in range(1,13):
    for b in range(1,13):
        print(f"{a} X {b} = {a * b}")
    print("===" * 30)

#assignment
# create a scientific calculator that performs the following operations
#addition, substraction,multiplication,division,power of the number, squareroot, modulus, integer division , logarithm,sine
# cosine tanget 