"""
Представлен список чисел. Определить элементы списка, не имеющие повторений. Сформировать итоговый массив чисел,
соответствующих требованию. Элементы вывести в порядке их следования в исходном списке.
Для выполнения задания обязательно использовать генератор.
Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
Результат: [23, 1, 3, 10, 4, 11]
"""
a = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]


def g(k):
    for i in range(len(k)):
        if k.count(k[i]) == 1:
            yield k[i]


print([el for el in g(a)])