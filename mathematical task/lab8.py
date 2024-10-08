#https://ivtipm.github.io/Programming/Glava20/index20.htm#z674
#Даны целые числа a1, ..., a10, целочисленная квадратная матрица
#порядка n. Заменить нулями в матрице те элементы с чётной суммой 
#индексов, для которых имеются равные среди a1, ..., a10.

__author__ ="Borisova Ekaterina IVT20"

import ar
import mth
import numpy as np

assert mth.calc8_2([4, 7, 7, 10, 10, 9, 3, 1, 1, 3], [[14, 3, 4], [9, 1, 12], [8, 12, 14]]) == [[14, 3, 0], [9, 0, 12], [8, 12, 14]]
assert mth.calc8_2([13, 2], [[5, 13, 6, 3], [14, 7, 12, 2], [12, 4, 2, 12], [6, 5, 6, 6]]) == [[5, 13, 6, 3], [14, 7, 12, 0], [12, 4, 0, 12], [6, 5, 6, 6]]
assert mth.calc8_2([14, 4, 6, 2, 9, 5, 3, 8, 3, 8], [[1, 14, 2], [6, 14, 5], [6, 11, 8]]) == [[1, 14, 0], [6, 0, 5], [0, 11, 0]]

n =int(input ("Введите количество элементов в квадратной матрице: "))

matrix = np.random.randint(low=1, high=15, size=(n, n))

a=[]

a = (ar.ar_filling(a, 10))
#matrix = (ar.mt_filling(a, n))

print(f'массив а', f'{a}', sep='\n')
print(f'матрица', f'{matrix}', sep='\n')

print('измененная матрица')
print (mth.calc8_2(a, matrix))

#print('старый способ')
#print (mth.calc8(a, matrix))