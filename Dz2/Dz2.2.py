""" Для списка реализовать обмен значений соседних элементов, т.е.Значениями обмениваются элементы
 с индексами 0 и 1, 2 и 3 и т.д.При нечетном количестве элементов последний сохранить на своем месте.
 Для заполнения списка элементов необходимо использовать функцию input().
"""

a = input('введите элементы списка через пробел: ').split()
i = 0
while i < len(a)-1:
    a[i], a[i + 1] = a[i + 1], a[i]
    i += 2
print(a)
