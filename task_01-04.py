import random


def is_valid(num):
    if num.isdigit():
        num = int(num)
        if 1 <= num <= 100:
            return True
        else:
            return False
    else:
        return False


def get_top_num():
    print('введите число до которого будем играть')
    top_num = input()
    if top_num.isdigit():
        top_num = int(top_num)
        if top_num > 2:
            return top_num
        else:
            return False
    else:
        return False


def get_min_attempts(num):
    counter = 0
    while num != 0:
        counter += 1
        num //= 2
    return counter


print('добро пожаловать в игру угадай число')
attempts_counter = 0
top_num = get_top_num()
secret_number = random.randint(1, top_num)

while True:
    print('введите число от 1 до', top_num)
    user_input = input()
    if not is_valid(user_input):
        continue
    user_number = int(user_input)
    attempts_counter += 1
    if secret_number > user_number:
        print('загаданное число больше')
    elif secret_number < user_number:
        print('загаданное число меньше')
    else:
        print('вы угадали за', attempts_counter, 'попыток. Оптимально нахождение за',
              get_min_attempts(top_num), 'попыток')
        print('хотите сыграть еще? y/n')
        if input() == 'y':
            attempts_counter = 0
            top_num = get_top_num()
            secret_number = random.randint(1, top_num)
            continue
        break
