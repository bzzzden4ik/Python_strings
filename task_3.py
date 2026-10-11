alp = 'abcdefghijklmnopqrstuvwxyzабвгдеёжзийклмнопрстуфхцчшщъыьэюя'

text = input('Введите текст: ').lower()

words_list = []
current_word = ''

for char in text:
    if char in alp:
        current_word += char
    elif current_word != '':
        words_list.append(current_word)
        current_word = ''

if current_word != '':
    words_list.append(current_word)

word_counts = {}

for word in words_list:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

items = list(word_counts.items())

sorted_words = sorted(items, key=lambda x: x[1], reverse=True)

count_to_show = min(len(sorted_words), 5)

print('Топ-5 самых частых слов:')

for i in range(count_to_show):
    word = sorted_words[i][0]
    count = sorted_words[i][1]
    
    print(f'{word} - {count} повторений')
