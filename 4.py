# number 1
s = input()
n = 'н'
count = 0
index = s.find(n)
while index != -1:
    count +=1
    n = n + 'н'
    index = s.find(n)
if count != 0:
    replace_n = '!'*count   
    n = n[:-1]
    s = s.replace(n, replace_n)
print(s, count)

# №2
s = 'yrtjnfas(dsok)'
print(((s.split("("))[1].split(")"))[0])

# number 3
s = input()
lst_1 = s.split(" ")
for i in lst_1:
    if i == ",":
        lst_1 = lst_1.split(",")
    else:
        break
for i in lst_1:
    if i[0] == 'а' or i[0] == 'А' and i[-1] == 'я':
        print(i, end=',')


def sum_n(n):
    sum = 0
    while n != 0:
        sum += n % 10
        n = n//10
    return sum
sum_n(int(input()))

def sum_d(n): #Определение функции с параметром
  sum = 0
  while n != 0:
    sum += n % 10
    n = n // 10
  return sum #Возврат значения функции

#Запуск программы
sum_d(int(input()))

    