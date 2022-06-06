#1
li = [9,1,8,2,7,3,6,4,5]

s_li =sorted(li)

print ('Sorted Variable :\t', )

li.sort()

print('Original Variable:\t', li)

# print('Original Variable:\t',)

# tup = (9,1,8,2,7,3,6,4,5)
# print('Tuple\t)

#2
li = [-6,-5,-4,1,2,3]
s_li = sorted(li, key=abs)
print (s_li)

#3
class Employee():
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return '({},{},${})'.format(self.name, self.age, self.salary)

from operator import attrgetter

e1 = Employee('Carol', 37, 70000)
e2 = Employee('Andre', 29, 80000)
e3 = Employee('Joao', 43, 90000)

employees = [e1,e2,e3]

def e_sort(emp):
    return emp.age

s_employees = sorted(employees, key=attrgetter('age'))

print(s_employees)