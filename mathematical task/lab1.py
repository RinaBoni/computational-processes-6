
#https://ivtipm.github.io/Programming/Glava01/index01.htm#z2
#Даны действительные числа x и y. Получить (|x| - |y|) / (1 + |xy|)

__author__ ='Borisova Ekaterina IVT20'


import math as m
import mth

assert 0 ==mth.calc1(1, 1)
assert 1.0 ==mth.calc1(1, 0)
assert -0.125 ==round(mth.calc1(-3, 5), 3)

x = float (input("Введите x: "))
y = float (input("Введите y: "))

result = mth.calc1(x, y)

print (f"Результат  {result: }")
#.3f

