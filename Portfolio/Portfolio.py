from math import *
from random import *
print("Arvuti mõistab numbrit 1-10 ja sina üritad seda ära arvata.")
a=randint(1,10)
vastus=int(input("mis arv on mõistatantud arvutit?: "))
k=p=1
while vastus!=a:
    print("Sa ei arvanud ära; proovi uuesti!:")
    vastus=int(input("Sisesta vastus: "))
    k+=1
    p+=1
    if k>2:
        print("Püüdlused on lõppenud")
        b=input("Proovi veel kord")
        if b.upper()=="JAH":
            k=0
            continue
        else:
            break
if a==vastus:
   print("Palju õnne, sa arvasid ära!",p)
print()

#2
while True:
    number = int(input("Sisestage number suurem kui 10: "))
    p+=1
    if number >=10:
        print("Õigesti")
        break
    else:
        print("Arv on liiga väike")
print("katsed", p)


#4
print("Ma tahan kommi")
katsed = 0
while True:
    answer = input("Tahan kommi!")
    katsed +=1
    if answer.lower() == "komm":
        print(f"Teil kommid kirjutatakse kulus {katsed} katse.")





#5
while True:
    try:
        nimi=input("Palun")
