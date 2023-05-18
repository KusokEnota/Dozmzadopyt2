"""Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. Пользователь в первой
строке вводит натуральное число N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai.
Последняя строка содержит число X
"""
N = int(input("Введите количество элементов в массиве: "))
A = []
for i in range(N):
    A.append(int(input("Введите число A[" + str(i + 1) + "]: ")))
X = int(input("Введите число X: "))

closest_element = A[0]
min_difference = abs(A[0] - X)

for element in A[1:]:
    difference = abs(element - X)
    if difference < min_difference:
        min_difference = difference
        closest_element = element
print("Самый близкий по величине элемент к заданному числу X:", closest_element)
