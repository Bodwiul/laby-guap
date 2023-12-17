#Реализовать модуль, содержащий функцию, которая вставляет в массив элемент с заданным индексом и заданным значением. Лишний элемент должен пропасть.
import message
while True:
    massiv = input('Введите элементы массива: ').split()
    if len(massiv) > 0:
        break
    else:
        print('Введите элементы ещё раз')

while True:
    try:
        index = int(input('Введите индекс, элемент которого хотите заменить: '))
        if index > 0:
            if index < len(massiv):
                break
        else:
            if abs(index) <= len(massiv):
                break
    except ValueError:
        print('Введите числовое значение')

while True:
    znachenie = input('Введите новое значение: ')
    if len(znachenie.split()) > 0:
        break
    else:
        print('Введите значение ещё раз')

print(message.zamena(massiv,index,znachenie))



