#1
import math 
def coord(x,y):
    return math.degrees(math.atan(x/y))
x1,x2 = map(float,input('Введите x1 и x2: ').split())
y1,y2 = map(float,input('Введите y1 и y2: ').split())
z1,z2 = map(float,input('Введите z1 и z2: ').split())
print(coord(x1,x2))
print(coord(y1,y2))
print(coord(z1,z2))

#2
def y(n_1):
  s=bin(n_1)[2:]
  s1=s[:(len(s))//2]
  s2=s[(len(s)-1)//2+1:]
  return s1[::-1]==s2
def f(n_1):
  v=n_1
  d=2
  if n_1==1:
    return False
  else:
    while d<=n_1//2:
      if n_1%d==0:
        v=0
      d+=1
    if v==0:
      return False
    else:
      return y(v)
n_1 = int(input('Введите n: '))
m=[]
for i in range(0,n_1+1):
  if f(i)==True:
      m.append(i)
print(m)