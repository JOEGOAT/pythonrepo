#JSON -> Javascript Object Notation
#To use python json module, you have to import it
import json

#If you want help regarding Json
#print(help(json))
print(dir(json))

#!. Converting to a python object (frm a JSON string)
# json object
person = """{
    "name":"Pach",
    "age":18,
    "city":"Juba"
}"""

# convert to Json string/object
# We use leads() to convert a python object to a json string
person_json_data = json.loads(person)
print(person_json_data)

#python object has single quotes while json string double quotes
print({"name":"Pach","age":18})

#2.Convert to json string
product = {
    'name':'Product 1',
    'code':'F9999',
    'price' : 159.99,
    'quality':6
}

person_json_data=json.dumps(product)
print(person_json_data)

#create a list of "person" dictionaries with a name,age and a list of hobbies for each person.
#Convert the list of persons to a json string

#Creating a person dictionary
persons=[
    {
    'name':'Joe',
    'age':20,
    'hobbies':['coding','dancing']
    },
    {
    'name':'Joe',
    'age':20,
    'hobbies':['UFC','swimming']
    },
    {
    'name':'Joe',
    'age':20,
    'hobbies':['painting','swimming']
    }
]

print(persons)

#extract painting
print(persons[2]['hobbies'][0])