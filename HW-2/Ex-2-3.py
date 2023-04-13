# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

# 10 -> 1 2 4 8

num = int(input("Введите число: "))
tmp = 0
deg = 0

while tmp < num:
    tmp = 2 ** deg
    if tmp > num:
        break
    deg += 1
    print(tmp, end=" ")