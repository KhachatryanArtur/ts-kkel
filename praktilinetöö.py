
from math import *
from random import *

#1
try:
    a=int(input("Sisesta arv"))
    if a>0:
        print("Positiivne")
        if a%2==0:
            print(f"{a} on paaris")
        else:
                print(f"{a} on paaritu")
    else:
        print("Negatiivne")
except:
    print("Vale andmetüüp")



#2
num1 = int(input("Первый номер: "))
num2 = int(input("Второй номер: "))
num3 = int(input("Третий номер: "))
if num1 > 0 and num2 > 0 and num3 > 0:
    if num1 + num2 + num3 == 180:
        # Является ли треугольник равносторонним, равнобедренным или разносторонним.
        if num1 == num2 and num2 == num3:
            print("Цифры обозначают углы равностороннего треугольника.")
        elif num1 == num2 or num1 == num3 or num2 == num3:
            print("Цифры обозначают углы равнобедренного треугольника.")
        else:
            print("Цифры обозначают углы разностороннего треугольника.")
    else:
        print("Не углы")
else:
    print("Ошибка")


    #3
kusimus = input("Хочешь узнать день недели? ")
if kusimus.lower() == "jah":
  number = input("Введите число от 1 до 7: ")
  if number.isdigit() and 1 <= int(number) <= 7:
    days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
    print(f"день недели: {days[int(number)-1]}")
  else:
    print("Ошибка")
    
from math import *
from pickle import TRUE
from random import *

#1
try:
    a=int(input("Sisesta arv"))
    if a>0:
        print("Positiivne")
        if a%2==0:
            print(f"{a} on paaris")
        else:
                print(f"{a} on paaritu")
    else:
        print("Negatiivne")
except:
    print("Vale andmetüüp")



#2
num1 = int(input("Первый номер: "))
num2 = int(input("Второй номер: "))
num3 = int(input("Третий номер: "))
if num1 > 0 and num2 > 0 and num3 > 0:
    if num1 + num2 + num3 == 180:
        # Является ли треугольник равносторонним, равнобедренным или разносторонним.
        if num1 == num2 and num2 == num3:
            print("Цифры обозначают углы равностороннего треугольника.")
        elif num1 == num2 or num1 == num3 or num2 == num3:
            print("Цифры обозначают углы равнобедренного треугольника.")
        else:
            print("Цифры обозначают углы разностороннего треугольника.")
    else:
        print("Не углы")
else:
    print("Ошибка")


    #3
kusimus = input("Хочешь узнать день недели? ")
if kusimus.lower() == "jah":
  number = input("Введите число от 1 до 7: ")
  if number.isdigit() and 1 <= int(number) <= 7:
    days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
    print(f"день недели: {days[int(number)-1]}")
  else:
    print("Ошибка")

#3
for I in range(10):
    print(I, end="; ")


for I in range(2, 12):
    print(I, end="; ")

for I in range(2, 12, 3):
    print(I, end="; ")

for I in range(12, 2, -2):
    print(I, end="; ")


print("Arvuta peast! ...4*100-55")

o_vastus=4*100-55
while True:
    if o_vastus==345 break
        if o_vastus<345:
            if o_vastus>345:


vastus=int(input("Lahenda ülesanne ..."))

k=1

while vastus!=o_vastus:

    print("Viga! Sisesta Õige vastus on ...", )

    vastus=int(input("Sisesta vastus ..."))

    k+=1

print("Õige vastus! Katsed oli ...",k )

x=0

while x<30:

    if x%2==1:

        print(x, end=" ")

    x+=1

