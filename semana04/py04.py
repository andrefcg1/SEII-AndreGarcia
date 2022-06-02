#1
courses = ['History', 'Math', 'Physics', 'CompSci']
print(len(courses))
print(courses)
print(courses[-2])
print(courses[0:2])#First inclusive, last isn't

#2
courses.append('Art')
print(courses)

#3
courses.insert(0,'French')
print(courses)

#4
courses = ['History', 'Math', 'Physics', 'CompSci']
courses_2 = ['Art', 'Education']

courses.insert(0,courses_2)

print(courses)

#5
courses = ['History', 'Math', 'Physics', 'CompSci']
courses_2 = ['Art', 'Education']

courses.extend(courses_2)

print(courses)

#6
courses = ['History', 'Math', 'Physics', 'CompSci']

courses.remove('Math')

print(courses)

#7
courses = ['History', 'Math', 'Physics', 'CompSci']

courses.pop()

print(courses)

#8
courses = ['History', 'Math', 'Physics', 'CompSci']

popped = courses.pop()
print(popped)

#9
courses.reverse()
print(courses)

#10
courses = ['History', 'Math', 'Physics', 'CompSci']

courses.sort()

print(courses)

#11
courses = ['History', 'Math', 'Physics', 'CompSci']
nums = [1, 5, 2, 4, 3]

courses.sort()
nums.sort()

print(courses)
print(nums)

#12
courses = ['History', 'Math', 'Physics', 'CompSci']
nums = [1, 5, 2, 4, 3]

courses.sort(reverse=True)
nums.sort(reverse=True)

print(courses)
print(nums)

#13
courses = ['History', 'Math', 'Physics', 'CompSci']
nums = [1, 5, 2, 4, 3]

sorted_courses = sorted(courses)

print(sorted_courses)

#14
courses = ['History', 'Math', 'Physics', 'CompSci']
nums = [1, 5, 2, 4, 3]

sorted_courses = sorted(courses)

print(min(nums))
print(max(nums))
print(sum(nums))

#15
courses = ['History', 'Math', 'Physics', 'CompSci']

print(courses.index('Math'))
print('Math' in courses)

#16
courses = ['History', 'Math', 'Physics', 'CompSci']

for item in courses:
    print(item)

#17
courses = ['History', 'Math', 'Physics', 'CompSci']

for index, course in enumerate(courses):
    print(index, course)

#18
courses = ['History', 'Math', 'Physics', 'CompSci']

course_string = ' - '.join(courses)

print(course_string)

#18
courses = ['History', 'Math', 'Physics', 'CompSci']

course_string = ' - '.join(courses)

new_list = course_string.split(' - ')

print(course_string)
print(new_list)

#19
list_1 = ['History', 'Math', 'Physics', 'CompSci']
list_2 = list_1

print(list_1)
print(list_2)

list_1[0] = 'Art'

print(list_1)
print(list_2)

#20
tuple_1 = ['History', 'Math', 'Physics', 'CompSci']
tuple_2 = tuple_1

print(tuple_1)
print(tuple_2)

tuple_1[0] = 'Art'

print(tuple_1)
print(tuple_2)

#21
cs_courses = {'History', 'Math', 'Physics', 'CompSci', 'Math'}

print('Math' in cs_courses)

#22
cs_courses = {'History', 'Math', 'Physics', 'CompSci', 'Math'}
art_courses = {'History', 'Math', 'Art', 'Design'}

print(cs_courses.intersection(art_courses))

#23
cs_courses = {'History', 'Math', 'Physics', 'CompSci', 'Math'}
art_courses = {'History', 'Math', 'Art', 'Design'}

print(cs_courses.difference(art_courses))

#24
cs_courses = {'History', 'Math', 'Physics', 'CompSci', 'Math'}
art_courses = {'History', 'Math', 'Art', 'Design'}

print(cs_courses.union(art_courses))

#25
empty_list = []
empty_list = list()

empty_tuple = []
empty_tuple = tuple()

empty_set = []
empty_set = set()