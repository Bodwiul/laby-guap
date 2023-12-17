while True:
    text = input("Введите текст: ")
    if len(text.split())>0:
        break
    else:
        print('Введите текст ещё раз:')

split_alf = '\t.,;?/!()'
for sym in split_alf:
    new_text = ''
    for word in text.split(sym):
        if not(' ' in word):
            word += ' '
            new_text += word
        else:
            new_text += word
    text = new_text

split_text = text.split()

for i in range(len(split_text)):
    for j in range(i + 1, len(split_text)):
        if split_text[i] == split_text[j] and len(split_text[i]) > 0:
            print(split_text[i])
            break


