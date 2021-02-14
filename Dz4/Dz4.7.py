"""
Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
При вызове функции должен создаваться объект-генератор. Функция должна вызываться следующим образом:
for el in fact(n). Функция отвечает за получение факториала числа, а в цикле необходимо выводить только
первые n чисел, начиная с 1! и до n!. Подсказка: факториал числа n — произведение чисел от 1 до n.
"""


def fact(n):
    f = 1
    for i in range(n):
        if i <= n:
            f *= i + 1
            yield f


for el in fact(int(input('Введите число: '))):
    print(el)


