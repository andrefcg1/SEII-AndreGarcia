#1
student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}

print(student)

#2
student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}

print(student['courses'])

#3
student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}

print(student.get['name'])

#4
student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}
student['phone'] = '555-5555'
student['name'] = 'Jane'

print(student)

#5
student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}

student.update({'name': 'Jane', 'age': 26, 'phone': '555-5555'0})

print(student)

#6
student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}

del student ['age']

print(student)

#7
student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}

age = student.pop('age')

print(student)
print(age)

#8
student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}

print(student.items())

#9
student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}

for key, value in student.items():
    print(key, value)