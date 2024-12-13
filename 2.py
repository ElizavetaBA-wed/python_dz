#1
a = int(input())
b = int(input())
if b == 0:
    print("Ошибка")
else:
    print(a/b)

# 2
sum = int(input('Введите стоимость в у.е \n'))
if sum > 20:
    sum = sum * 0.65
    print(f'стоимость покупки равна {round(sum, 2)}, размер скидки - 35%')
else:
    print(f'Стоимость покупки равна {sum}')

#3
b = int(input())
if b > 12 and b < 1:
    print('ошибка')
if b == 12:
    print('зима, декабрь')
if b == 1:
    print('зима, январь')
if b == 2:
    print('зима, февраль')
if b == 3:
    print('весна, март')
if b == 4:
    print('весна, апрель')
if b == 5:
    print('весна, май')
if b == 6:
    print("лето, июнь")
if b == 7:
    print('лето, июль')
if b == 8:
    print('лето, август')
if b == 9:
    print('осень, сентябрь')
if b == 10:
    print('осень, октябрь')
if b == 11:
    print('осень, ноябрь')


