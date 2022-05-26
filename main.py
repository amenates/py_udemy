# Вычисление квадратного корня, на примере вычисления площади треугольника
import math
a = 10
b = 5
c = 7
p = (a + b + c)/2
area = math.sqrt(p*(p-a)*(p-b)*(p-c))
area_2 = (p*(p-a)*(p-b)*(p-c)) ** 0.5
print(area)
print(area_2)
