import random


def generate_secret_word():
    digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    word = ''
    for i in range(4):
        random_index = random.randint(0, len(digits) - 1)
        word += str(digits[random_index])
        digits.pop(random_index)
    return word


def get_cow_count(user_input, secret):
    counter = 0
    for i in range(len(secret)):
        if user_input[i] != secret[i] and user_input[i] in secret:
            counter += 1
    return counter


def get_bulls_count(user_input, secret):
    counter = 0
    for i in range(len(secret)):
        if secret[i] == user_input[i]:
            counter += 1
    return counter


def validate_input(player_input):
    if player_input.isdigit():
        if len(player_input) == 4:
            test_set = set()
            for elem in player_input:
                test_set.add(int(elem))
            if len(test_set) != 4:
                print('необходимо ввести разные цифры')
                return validate_input(input())
        else:
            print('необходимо ввести 4 цифры')
            return validate_input(input())
    else:
        print('необходимо ввести цифры')
        return validate_input(input())
    return player_input


def init_game():
    secret_word = generate_secret_word()
    print(secret_word)
    while True:
        print('найди число, загаданное компьютером')
        user_word = validate_input(input())
        bulls_count = get_bulls_count(user_word, secret_word)
        cows_count = get_cow_count(user_word, secret_word)
        print(f'{bulls_count} быков, {cows_count} коров')
        if bulls_count == 4:
            print('ура, победа! ')
            break

    print('хотите еще сыграть еще? y/n')
    if input().lower() == 'y':
        init_game()


init_game()
