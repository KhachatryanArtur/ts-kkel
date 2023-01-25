from math import *
from random import *
#harjutus 0
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

#harjutus 23

ages = []

for i in range(10):
    age = int(input("Sisestage õpilase vanus: "))
    ages.append(age)

adult_count = 0
minor_count = 0

for age in ages:
    if age >= 18:
        adult_count += 1
    else:
        minor_count += 1

print("Täiskasvanute arv:", adult_count)
print("Alaealiste arv:", minor_count)



