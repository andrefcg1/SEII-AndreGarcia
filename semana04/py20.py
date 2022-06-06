""" #1
f = open('test_file.txt')
try:
    pass
except Exception:
    pass

#2
try:
    f = open('test_file.txt')
except Exception:
    print('Sorry. This file doesn not exist!')

#3
try:
    f = open('test_file.txt')
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print(e)

#4
try:
    f = open('test_file.txt')
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print(e)
else:
    print(f.read())
    f.close()
finally:
    print("Executing Finally...") """

#5
try:
    f = open('curruptfile.txt')
    if f.name == 'currupt_file.txt':
        raise Exception
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print('Error!')
else:
    print(f.read())
    f.close()
finally:
    print("Executing Finally...")

print('End of program')