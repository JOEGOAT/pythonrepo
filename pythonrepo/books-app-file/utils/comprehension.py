numbers = [1,2,3,4,5,6,7,8,9,10]

# copied_numbers = []
# for number in numbers:
#     copied_numbers.append(number)

#     print(copied_numbers)

# Easier way using list comprehension

# copied_numbers = [number  for number in numbers]
# print(copied_numbers)

#list comprehension with conditionals
# even_numbers = []
# for number in numbers:
#     if number % 2 == 0:
#         even_numbers.append(number)
# print(even_numbers)
# another way
even_numbers = [number for number in numbers if number % 2 == 0]
print(even_numbers)