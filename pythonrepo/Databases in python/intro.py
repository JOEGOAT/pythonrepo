import sqlite3 

#check the version
print(sqlite3.sqlite_version)

#create a demo database
db  = "demo db"

# connect to the database db
conn = sqlite3.connect(db)
#print(conn)

# create a cursor object to be able to perform CRUD OPERATION
cursor = conn.cursor()

# C -> Create 
# R -> Read 
#U -> Update
#D -> Delete
#create a table call it -> employees

query = '''
    CREATE TABLE IF NOT EXISTS employees
    (
        id integer PRIMARY KEY AUTOINCREMENT,
        full_name char(30) not null,
        age int not null,
        email char(50)
    )
'''
#execute the query
cursor.execute(query)
 
#commit changes
conn.commit()

#close the connection
# display a success message if table was created
print("Created Table Employees...")

#1 Create
#lets create employees
# create_query = "INSERT INTO employees(full_name,age,email) VALUES ('Employee 4',24,'employee1@email.com')"

# #execute query
# cursor.execute(create_query)

#commit changes
conn.commit()

print("Inserted Data")

#R -READ
#Let's read data frm the Database
#Create our read/fetch query
read_query = "SELECT id,full_name,age,email FROM employees"
read_query = "SELECT * FROM employees"

#execute our fetch_query
cursor.execute(read_query)

#Get all the employees frm the database
employees = cursor.fetchall

#display the results
# # print(employees)
# for employee in employees:
#     print(employee[1])

#fetch one record/employee
select_one_query ="SELECT *FROM employees"
cursor.execute(select_one_query)
employee = cursor.fetchone()
print(employee) 

#fetch many records/employees
select_many_query = "SELECT *FROM employees"
cursor.execute(select_many_query)
employee = cursor.fetchmany(3)
print(employee)

#Reading Data Using Parameters
params = (20,)

query = "SELECT *FROM employees WHERE AGE > ?"
cursor.execute(query,params)
employees_above_20 = cursor.fetchall()
print(employees_above_20)

#U - Update
update_query = "UPDATE employees SET age = ? WHERE email = ?"
cursor.execute(update_query,(28,"employee4@email.com"))
conn.commit()
update_employee = cursor.fetchone()
print(update_employee)

#D - Delete
#let's delete emplopyees
delete_query = "DELETE FROM employees WHERE id = ?"
cursor.execute(delete_query,(1,))
conn.commit()
