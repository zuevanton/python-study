def update_user_word(secret_word, user_word, char):
    new_user_word = ''
    for i in range(len(secret_word)):
        if secret_word[i] == char:
            new_user_word += char
        else:
            new_user_word += user_word[i]
    return new_user_word


secret_word = 'академия'
user_word = '********'
user_symbols = ''
attempts_counter = 0
print('отгадайте слово. где вы проходите обучение?')
print(user_word)

while user_word != secret_word:
    print('введите букву')
    user_char = input()
    if len(user_char) != 1 or not ord('а') <= ord(user_char.lower()) <= ord('я'):
        continue
    if user_char in user_symbols:
        print('вы уже вводили этот символ')
        continue
    user_symbols += user_char
    new_user_word = update_user_word(secret_word, user_word, user_char)
    attempts_counter += 1
    if user_word == new_user_word:
        print('такой буквы нет в слове')
    else:
        print('ура! такая буква есть')
    user_word = new_user_word
    print(user_word)

    if secret_word == user_word:
        print(f'ура, слово отгадано за {attempts_counter} попыток. хотите сыграть еще? да/нет')
        if input().lower() == 'да':
            secret_word = 'верстки'
            user_word = '*******'
            attempts_counter = 0
            user_symbols = ''
            print('чему обучаетесь?')
            print(user_word)
            continue

