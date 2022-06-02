#1
if True:
    print('Conditional was True')

#2
language = 'Python'

if language == "Python":
    print('Evaluated to True')

#3
language = 'Python'

if language == "Python":
    print('Language is Python')
else:
    print('No match')

#4
language = 'Python'

if language == "Java":
    print('Language is Python')
else:
    print('No match')

#5
language = 'Java'

if language == "Python":
    print('Language is Python')
elif language == "Java":
    print('Language is Java')
else:
    print('No match')

#6
user = 'Admin'
logged_in = True

if user == 'Admin' and logged_in:
    print('Admin Page')
else:
    print('Bad Creds')

#7
user = 'Admin'
logged_in = True

if user == 'Admin' or logged_in:
    print('Admin Page')
else:
    print('Bad Creds')

#8
user = 'Admin'
logged_in = True

if not logged_in:
    print('Please Log In')
else:
    print('Welcome')

#9
a = [1, 2, 3]
b = a

print(id(a))
print(id(b))
print(id(a == b))

#10
condition = 'False'

if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')
    
#11
condition = None

if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')

#12
condition = ''

if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')

#13
condition = {}

if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')

#14
condition = 'Test'

if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')