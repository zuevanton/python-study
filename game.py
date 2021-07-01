def create_field():
    field = []
    for i in range(3):
        field.append(['*'] * 3)
    return field


def print_field(field):
    for i in range(3):
        for j in range(3):
            print(field[i][j], end='')
        print()


def win(field):
    for i in range(3):
        if field[i][0] == field[i][1] == field[i][2] and field[i][0] != '*':
            return True
        if field[0][i] == field[1][i] == field[2][i] and field[0][i] != '*':
            return True
        if field[0][0] == field[1][1] == field[2][2] and field[0][0] != '*':
            return True
        if field[0][2] == field[1][1] == field[2][2] and field[2][0] != '*':
            return True
    return False


def end_game(field):
    if win(field):
        return True
    for i in range(3):
        for j in range(3):
            if field[i][j] == '*':
                return False

    return True


def validate_input(player_input):
    if player_input.isdigit():
        player_input = int(player_input)
        if 1 <= player_input <= 3:
            return player_input
        else:
            print('введите число от 1 до 3')
            return validate_input(input())
    else:
        print('введите число от 1 до 3')
        return validate_input(input())


def init_game():
    field = create_field()
    current_symbol = 'X'

    while not end_game(field):
        print_field(field)
        print('введите номер строки и столбца')
        row = validate_input(input())
        column = validate_input(input())
        if field[row - 1][column - 1] == '*':
            field[row - 1][column - 1] = current_symbol
        else:
            print('тут уже занято, повторите попытку')
            continue
        if current_symbol == 'X':
            current_symbol = 'O'
        else:
            current_symbol = 'X'

    if current_symbol == 'X':
        print('ура победил O')
    else:
        print('ура победил X')

    print('хотите сыграть еще? y/n')
    if input().lower() == 'y':
        init_game()


init_game()
