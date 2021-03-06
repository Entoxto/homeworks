"""
Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools. Обратите внимание,
что создаваемый цикл не должен быть бесконечным. Необходимо предусмотреть условие его завершения.
Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.
"""
from sys import argv
from itertools import count, cycle

name, number_1, number_2 = argv

number_1 = int(number_1)
number_2 = int(number_2)

print("Итератор, генерирующий целые числа, начиная с указанного:\n")
for el in count(number_1):
    if el > number_2:
        break
    else:
        print(el)

print("\nИтератор, повторяющий элементы некоторого списка, определенного заранее:")
print("Нажмите s, чтобы остановиться или любую другую кнопку, чтобы продолжить:\n")
iterator = cycle([1, 2, 3, 4, 5, "и заново:)"])
s = 0
while s != 's':
    print(next(iterator), end='')
    s = input()
