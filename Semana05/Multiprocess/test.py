from tabnanny import check
import numpy as np


# V = [10] #itens
# F = [2,6,7,8,20,10,11,12,22,3]  #ID vendedores
# C = [4]     # Clientes
# X = [8]     # Id de um dos vendedores

V = [2] #itens
F = [3, 6]  #ID vendedores
C = [8]     # Clientes
X = [3]     # Id de um dos vendedores

check_position = C[0]%len(F)
print(F[check_position])

result = np.where(np.array(F) == X)

distance = check_position-result[0]
len1 = len(F) - distance
len3 = len(F) + distance
if check_position > result[0]:
    print(len1[0])
elif check_position == result[0]:
    print(0)
else: 
    print(len3[0])
