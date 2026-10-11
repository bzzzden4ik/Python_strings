text = input("Введите текст: ")

words = []
temp = ''

for i in range(len(text)):
    if text[i] == ' ':
        words.append(temp)
        temp = ''
    else:
        temp += text[i]

if temp:
    words.append(temp)

print("Вывод слов из строки в обратном порядке")

for i in range(len(words) - 1, -1, -1):
    print(words[i], end=' ')

print("Вывод символов строки в обратном порядке:")

for i in range(len(text) - 1, -1, -1):
    print(text[i], end='')
