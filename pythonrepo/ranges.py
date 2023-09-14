#codeskulptor
r = range(10)
print(r,type(r))
#apply the list() function to the range
print(list(r))

#you can do indexing
print(r[0])
print(r[5])
print(r[-1])

#you can also verify if cerrtain elements are in the range using in and not in
print(10 in r)
print(1 not in r)

#you can aplly the index() method to find out index of certain element of the range
print(r.index(4))

#you cannot slice a range but you can convert the range to a list using list() function
# and then apply you slice
print(list(r)[2:5])