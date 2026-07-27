#open read write readwrite append
import os

filename = 'data.txt'
#open read write readwrite append

filename = 'data.txt'

with open(filename, 'a') as file:
    """
    Writing to a file
    """
    file.write("twende \n")

with open(filename, 'r') as file:
    print(file.read())

with open(filename, 'r') as file:
    print(file.readlines())

with open(filename, 'r') as file:
    print(file.readline())

print((lambda x :x.upper())('erick'))

def mapper(n):
    return n+n

numbers = [1, 3, 5, 7, 9]
doubler = map(mapper, numbers)
print(list(doubler))

print(list(map(lambda x: x+x, numbers)))

students = [("Emil", 25), ("Tobias", 22), ("Linus", 28)]

sorted_students = sorted(students, key = lambda item: item[-1])

sorted_students_by_name = sorted(students, key = lambda x: len(x[0]), reverse = True)

ages = [5, 8, 9]
filtered = filter(lambda x: x%2 != 0, ages )

print(list(filtered))