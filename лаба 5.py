#Квадратная матрица, симметричная относительно главной диагонали, задана верхним треугольником в виде одномерного массива.
# Восстановить исходную матрицу и напечатать по строкам.
while True:
    try:
        f_line = int(input('Введите длину первой строчки массива: '))
        if f_line > 0:
            break
        else:
            print('Введите положительное числовое значение')
    except ValueError:
        print('Введите числовое значение')

first_line = f_line
array = []
while f_line > 0:
    for i in range(f_line):
        while True:
            value = input('Введите значение: ')
            try:
                value = int(value)
                break
            except ValueError:
                print('Введите числовое значение')
        array.append(value)
    f_line -= 1
array2 = [[0] * first_line for i in range(first_line)]
count = 0

for i in range(first_line):
    for j in range(i, first_line):
        array2[i][j] = array[count]
        count += 1

for k in range(first_line):
    for l in range(k, first_line):
        array2[l][k] = array2[k][l]

for i in range(0, len(array2)):
    for i2 in range(0, len(array2[i])):
        print(array2[i][i2], end=' ')
    print()

diagonal = []
for i in range(first_line):
    diagonal.append(array2[i][i])

for k in range(first_line):
            diagonal.append(array2[k][first_line - 1 - k])

divider = sum(diagonal)
for i in range(first_line):
    if i % 2 != 0:
        for j in range(first_line):
            array2[i][j] = array2[i][j]/divider

print(' ')
for i in range(0, len(array2)):
    for i2 in range(0, len(array2[i])):
        print(array2[i][i2], end=' ')
    print()