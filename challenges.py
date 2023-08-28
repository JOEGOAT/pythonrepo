#first_name="paul"
#age=19
#print("Hello " + first_name + " you have lived for" + str(age*31536000 ) + "seconds equivalent to "  + str(age) + "years")

#1.prompt/convert their age in seconds
#user_name = input("Please enter your name:")
#user_age  = int(input("Enter you age:"))

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

#.write a python program that prompts the user to enter marks for 5 subject and then computes the average score.
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

#asks the user for the names of 5 students
#Students_names = (input("Pls enter the names of 5 students with no spaces separated with comma: "))

#stores the names in a list
#Students_list = Students_names.split(",")
#print(Students_list)

#another way
# #asks the user for the names of 5 students
# stud_1 = input("Enter the name of the first student: ")
# stud_2 = input("Enter the name of the second student: ")
# stud_3 = input("Enter the name of the third student: ")
# stud_4 = input("Enter the name of the fourth student: ")
# stud_5 = input("Enter the name of the fifth student: ")

# #create a lsit
# students = [stud_1, stud_2, stud_3, stud_4, stud_5]
# #create an empty list
# students = []

# #append the names to our list
# students.append(stud_1)
# students.append(stud_2)
# students.append(stud_3)
# students.append(stud_4)
# students.append(stud_5)

# print(students)

# #ask the user for an index
# student_index = int(input("Enter an index btwn 1 and 5,to display a student: "))

# #get the student frm the list
# student_name = students[student_index -1]

# #display the student name with their indexj
# print(f"{student_name} is at Index: {student_index}")

#Write a program that asks user for scores for 5 units then stores them in a list/tuple/set/dictionary. Then calculates the average mark of the student, the program then grades the student based on the average mark. Use the following range table to grade the student
#range          Grade
#80-100         A
#70-79          B
#60-69          C
#50-59          D
#0-49           F
#Print output in nice formart
print("\t\t\tCPL GRADING SYSTEM")
print("==="*20)

#variables
#Create an empty list
subjects=[]

#Create a grade variable
Grade=""

#User input
student_name=input("Please enter your name: ")

Unit1=float(input("Enter the score for Maths: "))
if Unit1 >=0 and Unit1<=100:
    subjects.append(Unit1)
else:
    print("Maths score must be btwn 0 and 100")

Unit2=float(input("Enter the score for English: "))
if Unit2 >=0 and Unit2<=100:
    subjects.append(Unit2)
else:
    print("Maths score must be btwn 0 and 100")

Unit3=float(input("Enter the score for Physics: "))
if Unit3 >=0 and Unit3<=100:
    subjects.append(Unit3)
else:
    print("Maths score must be btwn 0 and 100")

Unit4=float(input("Enter the score for Geography: "))
if Unit4 >=0 and Unit4<=100:
    subjects.append(Unit4)
else:
    print("Maths score must be btwn 0 and 100")

Unit5=float(input("Enter the score for History: "))
if Unit5 >=0 and Unit5<=100:
    subjects.append(Unit5)
else:
    print("Maths score must be btwn 0 and 100")

print("==="*20)


total_score=sum(subjects)
average_score=sum(subjects)/len(subjects)
print(average_score)

#Grading
if average_score >= 80 and average_score <= 100:
    Grade ="A"
elif average_score >=70 and average_score<=79:
    Grade ="B"
elif average_score>=60 and average_score<=69:
    Grade="C"
elif average_score>=50 and average_score<=59:
    Grade="D"
elif average_score>=0 and average_score<=49:
    Grade="F"
else:
    print("Invalid Score,Please enter valid marks!!!")

#Output the student info
if average_score>100:
    print("Invalid Score,Please enter valid marks!!!")
else:
    print(f"Hello {student_name}, You have scored {average_score}%, which is Grade {Grade}")

print("==="*20)