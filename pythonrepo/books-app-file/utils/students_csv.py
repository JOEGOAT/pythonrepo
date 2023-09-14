students = open("students.txt","r")
all_students = students.readlines()

#for student in all_students[1:]:
    #print(student.strip("\n"))

cleaned_student_data = []
for student in all_students[1:]:
    cleaned_student_data.append(student.strip("\n"))

for student_data in cleaned_student_data:
    data = student_data.split(",")
    student_name = data[0].capitalize()
    university = data[1].capitalize()
    degree = data[2].capitalize()
    print(f"{student_name} is studying {degree} at {university}")

new_student =",".join("Joe,KU,Software Development".split(","))
with open("students.txt","a") as f:
    f.write(f"{new_student} \n")


