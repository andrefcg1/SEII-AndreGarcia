#1
hi = 'Hello World'

#2
print('hi')
print(hi)

#3
print(len(hi))

#4
print(hi[3])

#5
print(hi[0:5])

#6
print(hi[6:])

#7
print(hi.upper())
print(hi.count(hi))
print(hi.find('World'))

#8
ola = hi.replace('World', 'Universe')
print(ola)

#9
greeting = 'Sup'
name = 'Ronaldinho'
#message = greeting + ', ' + name + '. Deboas?! '
#print(message)
#message = '{}, {}. Deboas?!'.format(greeting, name)
#print(message)

#10
message = f'{greeting}, {name.upper()}. Deboas?!'
print(message)

#11
greeting = 'Sup'
name = 'Ronaldinho'

print(dir(name))

#12
greeting = 'Sup'
name = 'Ronaldinho'

print(help(str.lower))