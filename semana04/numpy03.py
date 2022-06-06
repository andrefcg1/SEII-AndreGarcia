import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

a1 = np.array([3,5,7,3])
a2 = np.zeros(10)
a3 = np.ones(10)
a4 = np.random.random(10)
a5 = np.random.randn(10)
a6 = np.linspace(0,10,100)
a7 = np.arange(0,10,0.02)

# a1[2]
# a1[2:]
# a1[:-2]
# a1[1:-2]
# a1>3

names = np.array (['Jim', 'Luke', 'Josh', 'Pete'])
first_letter_j = np.vectorize(lambda s: s[0])(names)=='J'
names[first_letter_j]

# print(first_letter_j)
# print(names)

f = lambda s: s[0]

# print(f('animal'))

print(a1%4 == 0)
