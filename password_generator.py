import random

print('это генератор паролей')


def ask_question(question):
    print(question, 'нажмите да или нет')
    answer = input()
    if answer.lower() == 'да':
        return True
    else:
        return False


def generate_password(length, chars):
    password = ''
    for i in range(length):
        random_index = random.randint(0, len(chars) - 1)
        password += chars[random_index]
    return password


def init():
    print('сколько вариций пароля вам нужно?')
    passwords_count = input()
    if passwords_count.isdigit() and int(passwords_count) > 0:
        passwords_count = int(passwords_count)
    else:
        passwords_count = 1

    print('введите длину пароля')
    length = input()
    if length.isdigit() and int(length) > 3:
        length = int(length)
    else:
        length = 8

    digits_enabled = ask_question('включать ли цифры?')
    latin_lowercase_enabled = ask_question('включать ли строчные латинские буквы?')
    latin_uppercase_enabled = ask_question('включать ли заглавные латинские буквы?')
    russian_lowercase_enabled = ask_question('включать ли строчные русские буквы?')
    russian_uppercase_enabled = ask_question('включать ли заглавные русские буквы?')
    punctuations_enabled = ask_question('включать ли знаки пунктуации?')

    enabled_chars = ''
    digits = '1234567890'
    latin_lowercase = 'abcdefghijklmnopqrstuvwxyz'
    latin_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    russian_lowercase = 'абвгдеёжзиклмнопрстуфхцчшщъыьэюя'
    russian_uppercase = 'АБВГДЕЁЖЗИКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    punctuations = '!#$%&*+-=?@^_'

    if digits_enabled:
        enabled_chars += digits
    if latin_lowercase_enabled:
        enabled_chars += latin_lowercase
    if latin_uppercase_enabled:
        enabled_chars += latin_uppercase
    if russian_lowercase_enabled:
        enabled_chars += russian_lowercase
    if russian_uppercase_enabled:
        enabled_chars += russian_uppercase
    if punctuations_enabled:
        enabled_chars += punctuations

    for i in range(passwords_count):
        print(generate_password(length, enabled_chars))
    if ask_question('сгенерировать новый пароль?'):
        return init()


init()
