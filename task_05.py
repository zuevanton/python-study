print('введите верхнюю границу')
last_num = int(input())
first_num = 1
print(f'задумайте число от 1 до {last_num}')
while True:
    attempt = (first_num + last_num) // 2
    print(f'число {attempt} то что мы ищем? введите больше / меньше / верно ?')
    player_answer = input()
    if player_answer == 'верно':
        print('ура, число отгадано')
        break
    elif player_answer == 'меньше':
        last_num = attempt
    elif player_answer == 'больше':
        first_num = attempt
    else:
        print('ошибка ввода')
        break
