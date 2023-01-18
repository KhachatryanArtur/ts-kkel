from math import *
from random import *


#первое задание(второй вариант)
a=int(input("valige number 1 kuni 9: "  ))
pin=["   (\_/)",
     "   (o o)",
     "   / | \*",]
for i in pin:
    print(i*a)



#второе задание(второй вариант)
L=int(input("Sisestage numbri: "))
sum=0
for i in range(L+1):
    sum+=i
print("Numbrite summa 1 kuni {L} on:", sum)


#третье задание(второй вариант)
print("Arvuti mõistab numbrit 1-100 ja sina üritad seda ära arvata.")
n = randint(0, 100)
i = 0
while True:
    a = int(input())
    if a == n:
        print("Sina võitsid")
        break
    if a < n:
        print("peidetud arv on suurem")
    else:
        print("peidetud arv on väiksem")
    i += 1
    if i == 10:
        print(f"Sa kaotasid. Varjatud number {n}")
        break



#пятое задание(второй вариант)
n = int(input("Sisestage numbri"))
sum = 0
mult = 1
while n > 0:
    digit = n % 10
    sum = sum + digit
    mult = mult * digit
    n = n // 10
print("Summa:", sum)
print("Korrutus:", mult)


