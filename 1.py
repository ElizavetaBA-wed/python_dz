1
import math
r = int(input('Введите радиус \n'))
l = 2 * math.pi * r
s = math.pi *  math.sqrt(r)
print(f'Длина круга равна {round(l, 2)}, Площадь круга - {round(s, 2)}')

2
x = 10 
y = 15
print(f'Переменные до: x = {x}, y = {y} ')
x, y = y, x
print(f'Переменные после: x = {x}, y = {y}')

3
import math
L = int(input('Введите длину маятника \n'))
g = 9.81
Lg = L/g
T = 2 * math.pi * math.sqrt(Lg)
print(f'Период равен {round(T, 2)}')
  