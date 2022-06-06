#1
import os

print(dir(os))

#2
import os

os.chdir('/Users/andre/Desktop/')

os.mkdir('Os-Demo-2')
# os.makedirs('Os-Demo-2')

print(os.listdir())

#3
import os

os.chdir('/Users/andre/Desktop/')

# os.mkdir('Os-Demo-2')
os.makedirs('Os-Demo-2/Sub-Dir-1')

print(os.listdir())

#4
import os

os.chdir('/Users/andre/Desktop/')

#os.rmdir('Os-Demo-2')
os.removedirs('Os-Demo-2/Sub-Dir-1')

print(os.listdir())

#5
import os

os.chdir('/Users/andre/Desktop/')

os.rename('test.txt','demo.txt')

print(os.listdir())

#6
import os

os.chdir('/Users/andre/Desktop/')

os.stat('demo.txt')
print(os.stat('demo.txt'))

#print(os.listdir())

#7
import os
from datetime import datetime

os.chdir('/Users/andre/Desktop/')

mod_time = os.stat('demo.txt').st_mtime
print(datetime.fromtimestamp(mod_time))

print(os.listdir())

#8
import os
from datetime import datetime

os.chdir('/Users/andre/Desktop/')

for dirpath, dirnames, filenames in os.walk('/Users/andre/Desktop/'):
    print('Current Path:', dirpath)
    print('Directories:', dirnames)
    print('Files:', filenames)
    print()

#9
import os
from datetime import datetime

os.chdir('/Users/andre/Desktop/')

print(os.environ.get('HOME'))

file_path = os.environ.get('HOME') + 'test.txt'
print(file_path)

#10
import os
from datetime import datetime

os.chdir('/Users/andre/Desktop/')

# print(os.environ.get('HOME'))

file_path = os.path.join(os.environ.get('HOME') + 'test.txt')
print(file_path)