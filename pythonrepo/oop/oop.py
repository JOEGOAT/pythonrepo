# OOP -> Object-Oriented Programing
# Modelling things in form of objects

# object -> a real world entity
#       -> an instance of a class
#       -> object can also be refered to an instance of a defined class and attribute values for a particular object       defining the state of that object

# class is a tempelate or blueprint that is used to create an object
#       -> a data containing its own variables,attributes and functions(functions in oop are refered to methods)
#       -> a standard definition of a class would tell you that a class is a blueprint for creating objects

# eg -> a blueprint of a house is a class,then the real house that will be built is an object
# eg 2 -> Human is a class -> then we can create many people from human class

# Inheritance -> This is when a class may inherit (acquire) all the names and functionalities from an existing class

# syntax for a class
#class class_name:
#    pass

# The __init__ method
# The special __init__method is a class constructor
# The word init should be proceeded and followed by double underscore(__)
# The role of __init__ is to initialize some variables and the method is called whenever you create a new instance of the class in which it resides
# actually it is the first code that is executed whenever you create a new instance of the class
# Any special method or regular method within a class is defined using def keyword as you would with regular functions
# The diffrence here is that each time you define a method inside a class, the first parameter inside the paranthesis is self
# self is no more than just a reference to the current instance of the current.
# After typing self , you define any other parameters that you want to be defined and initialized whenever you create a new instance of tha class which it resides 

class myRouter(object):
    "This is a class that describes the characteristics of a router"
    def __init__(self,routerName,model,serialNo,ios):
        self.routerName = routerName
        self.serialNo = serialNo
        self.model = model
        self.ios = ios

    def print_router(self, manuf_date):
        print("The Router Name is: ",self.routerName)
        print("The Router Model is: ",self.model)
        print("The Serial Number of the Router  is: ",self.routerName)
        print("The IOS Version is: ",self.ios)
        print("The model and date combined :",self.model + " " + manuf_date)

#Create our first object
#to create an object , you simply typ[e the class name and enter the a arguments required by the __init__ method in between the paranthesis - all of them except , except self, which is automitacally  passed by python
#router1 = myRouter("R1","2240","1223","12.6")
#what can we do with  this object?
#first, you can access each of its attributes
# print(router1.routerName)
# print(router1.model)
# print(router1.serialNo)
# print(router1.ios)


# what else
#router1.print_router("9/11/2023")

#btw to print time is
#from datetime import datetime
#print(datetime.now())

#router2 = myRouter("R2","7200","2323" ,"12.2")
#router2.print_router("4/4/2004")

# INHERITANCE
class myNewRouter(myRouter):
    def __init__(self,routerName,model,serialNo,ios,portsNo):
        myRouter.__init__(self,routerName,model,serialNo,ios)
        self.portsNo = portsNo

    def print_new_router(self,string):
        print(string + self.model)
newRouter = myNewRouter("newR1","1800","11115","12.2","10")
newRouter.print_router("-123")