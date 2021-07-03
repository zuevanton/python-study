import random

questions = []
answers = []


def create_data():
    global questions
    questions = [
        'сколько будет два плюс два умноженное на два?',
        'бревно нужно распилить на 10 частей. сколько нужно сделать распилов',
        'на двех руках 10 пальцев, соклько пальцев на 5 руках?',
        'укол делают каждые полчаса, сколько нужно минут для трех уколов?',
        'пять свечей горело, две потухли. сколько осталось свечей?',
    ]
    global answers
    answers = [6, 9, 25, 60, 2]


def get_result(right_answers, total_answers):
    result = [
        'Идиот',
        'Кретин',
        'Дурак',
        'Нормальный',
        'Талант',
        'Гений'
    ]
    for i in range(6):
        if right_answers / total_answers <= (i + 1) / 6:
            return result[i]


def print_scoreboard():
    file = open('game_results.txt', 'r')
    print(f'Имя       кол-во правильных ответов   результат')
    for line in file:
        line_list = line.strip('\n').split('-')
        name = line_list[0]
        right_answers = line_list[1]
        result = line_list[2]
        print(f'{name:10}{right_answers:28}{result}')
    file.close()


def save_game_result(user_name, right_answers, result):
    file = open('game_results.txt', 'a')
    file.write(f'{user_name}-{right_answers}-{result}\n')
    file.close()


def validate_user_answer(user_input):
    if not user_input.isdigit():
        print('нужно ввести число')
        return validate_user_answer(input())
    return int(user_input)


def init_test():
    right_answers_counter = 0
    create_data()
    total_questions = len(questions)
    print('как вас зовут?')
    user_name = input()
    for i in range(len(questions)):
        random_index = random.randint(0, len(questions) - 1)
        print(f'№{i + 1}. {questions[random_index]}')
        user_answer = validate_user_answer(input())
        if user_answer == answers[random_index]:
            right_answers_counter += 1
        questions.pop(random_index)
        answers.pop(random_index)
    save_game_result(user_name, right_answers_counter, get_result(right_answers_counter, total_questions))
    print(f'Верных ответов: {right_answers_counter}. Вы, {user_name} - {get_result(right_answers_counter, total_questions)}.')
    print('хотите повторить попытку? y/n')
    if input().lower() == 'y':
        init_test()


init_test()
print_scoreboard()