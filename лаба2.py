text = input("Введите текст: ")
split_alf = '.,;?/!()'
for sym in split_alf:
    new_text = ''
    for word in text.split(sym):
        if not(' ' in word):
            word += ' '
            new_text += word
        else:
            new_text += word
    text = new_text

split_text = text.split(' ')
print(split_text)
for i in range(len(split_text)):
    for j in range(i + 1, len(split_text)):
        if split_text[i] == split_text[j] and len(split_text[i]) > 0:
            print(split_text[i])
            break