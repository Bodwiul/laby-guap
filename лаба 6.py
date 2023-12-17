#Написать программу для объединения нескольких текстовых файлов в один файл с возможностью сокращения размера выходного файла.

while True:
    try:
        c = int(input('Введите количество файлов: '))
        if c > 0:
            break
        else:
            print('Введите положительное числовое значение')
    except ValueError:
        print('Введите числовое значение')


for i in range(c):
    newfile = open('text ' + str(i+1) + '.txt','w', encoding='utf-8')
    newfile.write(input('Введите текст:'))
    newfile.close()


mega_file = open('mega_file.txt', 'w+', encoding='utf-8')

text = ''
for j in range(c):
    file = open('text ' + str(j+1) + '.txt','r', encoding='utf-8')
    text += file.read() + ' '
    file.close()

mega_file.write(text)
mega_file.close()
mega_file = open('mega_file.txt', 'r', encoding='utf-8')

print(mega_file.read())
mega_file.close()