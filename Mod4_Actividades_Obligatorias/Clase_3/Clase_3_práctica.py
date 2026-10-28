import numpy as np
numeros = np.array([1, 2, 3, 4, 5])
print(numeros)  
print(numeros * 2)
a = np.array([10, 20, 30])
b = np.array([1, 2, 3])
a + b          # 11 22 33       suma elemento a elemento
a - b          # 9 18 27        resta
a * b          # 10 40 90       multiplicación
np.mean(a)     # 20.0             promedio
np.sum(a)      # 60               suma total
np.max(a)      # 30               valor maximo
np.min(a)      # 10               valor minimo
np.std(a)      # 8.16...          desviacion estandar
print (np.mean(a))
print (np.sum(a))
print (np.max(a))
print (np.min(a))
print (np.std(a))