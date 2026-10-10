text = input()

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

for i in range(len(words) - 1, -1, -1):
    print(words[i], end=' ')

print()

for i in range(len(text) - 1, -1, -1):
    print(text[i], end='')
