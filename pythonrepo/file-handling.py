import os

# working with files in python

#we use the open() function when working with files
#the open() function takes in 2 parameters when you want to open a file
#the params:
#1. -> filename(name of the file that you want to open)
#2. -> mode (mode that you want to open the file with)

#we have several modes:
#1. read -> 'r' : opens a file for reading and raises an error if the file doesnt exist
#2. append -> 'a' : opens a file to append to it , creates the file if it doesnt exist
#3. write -> 'w' : opens a file to write to it, overwrites the existing content, creates the file if it doesnt exist
#4. create -> 'x' : creates a new file

#open("fruits.txt", "x")

#1. Reading from a file
# file = open("fruits.txt", "r")
# file_contents = file.read()
# file.close()
# print (file_contents)

#2.appending to a file
#fruit = "dates"
# file = open("fruits.txt","a")
# file.write(fruit + "\n")
# file.close()

#3.writing to file
# file = open('fruits.txt','w')
# fruit = "oranges"
# file.write(f"{fruit}\n")
# file.close()

#4.deleting a file
#os.remove("fruits.txt")

import json
# 1.write a short python script which query the user for input(infinite loop with an exit possibility ) and writes the input to a file

# running = True

# while running:
#     print("Please choose")
#     print("1: Add Input")
#     print("q: Quit")

#     #Get user input
#     user_input = input("Your Choice: ")
#     if user_input == "1":
#         data_to_store = input("Please provide your input:")
#         with open("sample.txt" , "a" ) as f:
#             f.write(data_to_store)
#             f.write("\n")
    
#     elif user_input =='q':
#         running = False

# 2.and another option to your user interface:The user should be able to output the data stored in the file in the terminal 

running = True

while running:
    print("Please choose")
    print("1: Add Input")
    print("2: Output Data")
    print("q: Quit")

    #Get user input
    user_input = input("Your Choice: ")
    if user_input == "1":
        data_to_store = input("Please provide your input:")
        with open("sample.txt" , "a" ) as f:
            f.write(data_to_store)
            f.write("\n")
    
    elif user_input == "2":
        with open("sample.txt", "r") as f:
            #file_content = f.read()
            #print(file_content)

        # another way for a clean output

            file_content = f.readlines() #-> fto get list
            print(file_content)
            for line in file_content:
                print(line.strip("\n"))

    elif user_input =='q':
        running = False

#3.store the user input in alist(instead of directly adding it to a file) and write that list to the file ->using JSON and PICKLE

running = True

user_input_list = []
while running:
    print("Please choose")
    print("1: Add Input")
    print("2: Output Data")
    print("q: Quit")

    #Get user input
    user_input = input("Your Choice: ")
    if user_input == "1":
        data_to_store = input("Please provide your input:")
        user_input_list.append(data_to_store)
        with open("sample.txt" , "w" ) as f:
            f.write(json.dumps(user_input_list))
    
    elif user_input == "2":
        with open("sample.txt", "r") as f:
            file_content = json.loads(f.read)
            print(file_content)
            for line in file_content:
                print(line.strip("\n"))

    elif user_input =='q':
        running = False

#context managers -> open and close the file
# with open("fruits.txt", "a") as f:
#     content = "Python is cool" 
#     f.write(content)

# with open("fruits.txt","r") as f:
#     contents = f.read()
#     print(contents)

# file_name = "students.txt"

# #with open(file_name , "x") as f:
# #students = ["pach","ian","praise","lewis"]

# student = "pach"
            
# with open(file_name, "w") as f:
#     f.write(student)