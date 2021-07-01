import random

questions = []
answers = []
result = []


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
    global result
    result = [
        'Идиот',
        'Кретин',
        'Дурак',
        'Нормальный',
        'Талант',
        'Гений'
    ]


def init_game():
    right_answers_counter = 0
    create_data()
    print('как вас зовут?')
    name = input()
    for i in range(len(questions)):
        random_index = random.randint(0, len(questions) - 1)
        print(f'№{i + 1}. {questions[random_index]}')
        user_answer = int(input())
        if user_answer == answers[random_index]:
            right_answers_counter += 1
        questions.pop(random_index)
        answers.pop(random_index)

    print(f'Верных ответов: {right_answers_counter}. Вы, {name} - {result[right_answers_counter]}.')
    print('хотите повторить попытку? y/n')
    if input().lower() == 'y':
        init_game()


init_game()
