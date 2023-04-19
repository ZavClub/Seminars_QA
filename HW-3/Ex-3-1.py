# # Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A. Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai (можно использовать псевдогенерацию). Последняя строка содержит число X.
# *Пример:*

#  5            длинна массива
#  7 -2 3 5 1   произвольный массив
#  3            Какое число ищем, сколько раз оно повторяется
#  -> 1         количество совпадений


import random

arr_length = int(input("Введите длину массива: "))
srh_num = int(input("Введите искомое число: "))

rand_list = []

for i in range(arr_length):
    nums = random.randint(-10, 10)
    rand_list.append(nums)

print(rand_list)

for i in range(arr_length - 1):
    for j in range(arr_length - i - 1):
        if rand_list[j] > rand_list[j + 1]:
            rand_list[j], rand_list[j + 1] = rand_list[j + 1], rand_list[j]


print(rand_list)

tmp1 = arr_length[0]
for i in range(arr_length - 1):
    tmp2 = arr_length[i + 1]
    if tmp1 == tmp2:
        sum += 1
        tmp_num = arr_length[i]
    else:
        sum = 1
print(tmp_num)
