lower_alp = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
upper_alp = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')

text = input('Введите текст: ')

max_len = 0
current_len = 0

for char in text:
    if char in lower_alp or char in upper_alp:
        current_len += 1
    else:
        max_len = max(max_len, current_len)
        current_len = 0

K = max_len
result_list = []

for char in text:
    if char in lower_alp:
        idx = 0

        for i in range(26):
            if lower_alp[i] == char:
                idx = i

        new_idx = (idx + K) % 26
        result_list.append(lower_alp[new_idx])
    elif char in upper_alp:
        idx = 0

        for i in range(26):
            if upper_alp[i] == char:
                idx = i

        new_idx = (idx + K) % 26
        result_list.append(upper_alp[new_idx])
    else:
        result_list.append(char)

encrypted_text = ""

for char in result_list:
    encrypted_text += char

print('Зашифрованный текст: ', encrypted_text, '\nЧисло K: ', K, sep='')
