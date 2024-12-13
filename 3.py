
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

        
n = int(input())
sum = 0
for i in range(n+1):
    sum=+i *i *i
print(sum)


for i in range(10):
    for j in range(10):
        print("%4d" % (i * j), end="")
    print()









 
