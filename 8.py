
#1
import re
num = input()
if num[0].isalpha() and num [1].isdigit():
    car = re.findall(r"\b[АВЕКМНОРСТУХ]{1}\d{3}[АВЕКМНОРСТУХ]{2}\d{2,3}\b", num)
    print(f'Номер {num} - легковой')
if num[0].isalpha() and num[1].isalpha():
    taxi = re.findall(r"\b[АВЕКМНОРСТУХ]{2}\d{2,3}\b", num)
    print(f'Номер {num} - легковой')

    
#2
print('\n#2')

import re
from functools import reduce
file = open('Занятие_8_Текст.txt', 'r', encoding='utf-8')
s = file.readlines()
words= reduce(lambda x,y:  x[:-1]+' '+y, s).split()
print(words)
print(list(filter(lambda x: re.fullmatch(r'\b[А-Яа-яёЁ]+[-]?[А-Яа-яёЁ]+\b',x) or re.fullmatch(r'\b[A-Za-z]+[-]?[A-Za-z]+\b',x), words)))

#3
print('\n#3')

import re
from functools import reduce
s='Уважаемые! Если вы к 09:00 не вернёте чемодан, то уже в 09:00:01 я за себя не отвечаю.'
s=s.split()
x=list(filter(lambda x: re.search(r'\b(0[0-9]|1[0-9]|2[0-4])[:](0[0-9]|[0-9]{2})\b',x) ,s))
s= reduce(lambda x,y:  x+' '+y, s)
for i in x:
    s=s.replace(i,'(TBD)',1)
print(s)

