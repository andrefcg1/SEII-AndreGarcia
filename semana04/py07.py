#1
nums = [1, 2, 3, 4, 5]

for num in nums:
    print(num)

#2
nums = [1, 2, 3, 4, 5]

for num in nums:
    if num ==3:
        print('Found!')
        break
    print(num)

#3
nums = [1, 2, 3, 4, 5]

for num in nums:
    if num ==3:
        print('Found!')
        continue
    print(num)

#4
nums = [1, 2, 3, 4, 5]

for num in nums:
    for letter in 'abc':
        print(num, letter)

#5
for i in range(1, 11):
    print(i)

#6
x = 0

while x < 10:
    print(x)
    x += 1

#7
x = 0

while x < 10:
    if x ==5:
        break
    print(x)
    x += 1

#8
x = 0

while True:
    # if x == 5:
    #     break
    print(x)
    x += 1