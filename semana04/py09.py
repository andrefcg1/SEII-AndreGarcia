#1
import my_module as mm

courses = ['History', 'Math', 'Physics', 'CompSci']

index = mm.find_index(courses, 'Math')
print(index)

#2
index = mm.find_index(courses, 'Math')
print(index)

#3
from my_module import find_index

courses = ['History', 'Math', 'Physics', 'CompSci']

index = mm.find_index(courses, 'Math')
print(index)
print(test)

#4
from my_module import find_index as fi, test

courses = ['History', 'Math', 'Physics', 'CompSci']

index = fi(courses, 'Math')
print(index)
print(test)

#5
from my_module import *

courses = ['History', 'Math', 'Physics', 'CompSci']

index = fi(courses, 'Math')
print(index)
print(test)

#6
from my_module import find_index, test

courses = ['History', 'Math', 'Physics', 'CompSci']

index = find_index(courses, 'Math')
# print(index)
# print(test)

print(sys.path)

#7
import sys
sys.path.append('/Modules')  
from my_module import find_index, test

courses = ['History', 'Math', 'Physics', 'CompSci']

index = find_index(courses, 'Math')
# print(index)
# print(test)

print(sys.path)

#8
import random

courses = ['History', 'Math', 'Physics', 'CompSci']

random_course = random.choice(courses)

print(random_course)

#9
import random

courses = ['History', 'Math', 'Physics', 'CompSci']

rads = math.radians(90)

print(math.sin(rads))

#10
import datetime
import calendar

courses = ['History', 'Math', 'Physics', 'CompSci']

today = datetime.date.today()
print(today)

#11
import os

courses = ['History', 'Math', 'Physics', 'CompSci']

print(os.getcwd())