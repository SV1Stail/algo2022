#Сумма чисел в массиве.
'''n,old=int(input()),input().split()
mas=list(map(int,old))
x=0
for i in range(n):
    x+=mas[i]
print(x)'''


#Позиция максимума.
'''n,old=int(input()),input().split()
mas=list(map(int,old))
max_in_mas=max(mas)
print(mas.index(max_in_mas)+1)'''
#Префиксные суммы  ен прошёл 35 и далее тесты
'''import sys
input = sys.stdin.readline
n,q= map(int, input().split())
mas=list(map(int,input().split()))
ans=[0]*q
for i in range(q):
    l,r=map(int,input().split())
    ans[i]=sum(mas[l-1:r])
print(*ans,sep='\n')'''

#Максимальная сумма
'''import sys
input = sys.stdin.readline
n=int(input())
mas=list(map(int,input().split()))
maxx = 0
here = 0

for i in range(n):
    here = max(here + mas[i], 0)
    maxx = max(here, maxx)
if maxx==0:
    print(max(mas))
else:
    print(maxx)
'''
#20k20.

import sys
input = sys.stdin.readline
year=str(input().strip())
cnt_on_year=len(year)
mas_year=[0]*cnt_on_year #массив с разделенными цифрами года
mas_proverka=[] #сюда записываю пвторяющиеся значения


def povtorenie(x):
    for i in range(len(x)):
        if x[i] in x[i+1:-1]:
            return 1

for i in range(cnt_on_year):
    mas_year[i]=int(year[i])

for i in range(cnt_on_year):
    while (mas_year[i] in mas_year[i+1:-1]) or (mas_year[i] in mas_year[0:i]) or (mas_year[i]==0) or (mas_year[i]==2):
        mas_year[i]+=1
if (povtorenie(mas_year)!=1) and (0 not in mas_year) and (2 not in mas_year) and (cnt_on_year<=9):
    print(*mas_year,sep="")
else:
    print("1")
        
