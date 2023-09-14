import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sqlite3

#check the version of pandas installed
#print(pd.__version__)

#let's create a list
#people=[]

#let's create a dictionary
courses ={
    "course_name": ["Python","Pandas","Java","PHP"],
    "course_fee": [45000,40000,45000,45000],
    "duration": ["25days","23days","30days","26days"]
}

#create the datadrames indexes
index_labels=["a1","a2","a3","a4"]


#create a pandas dataframe
df=pd.DataFrame(data=courses,index=index_labels)

#print(df)
#create a db connection
conn=sqlite3.connect("cinema.db")

print(sqlite3.sqlite_version)

query="SELECT * FROM seat"

dataframe=pd.read_sql(query,conn)

#scatter graph
dataframe.plot(x="seat_id",y="price",kind="hist")
plt.show()


print(dataframe)