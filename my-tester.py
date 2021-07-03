import random


class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer


class QuestionsStorage:
    def get_questions(self):
        return [
            Question('сколько будет два плюс два умноженное на два?', 6),
            Question('бревно нужно распилить на 10 частей. сколько нужно сделать распилов', 9),
            Question('на двех руках 10 пальцев, соклько пальцев на 5 руках?', 25),
            Question('укол делают каждые полчаса, сколько нужно минут для трех уколов?', 60),
            Question('пять свечей горело, две потухли. сколько осталось свечей?', 2)
        ]


class Filesystem:
    def __init__(self, filepath):
        self.filepath = filepath

    def get_data(self):
        file = open(self.filepath, 'r')
        data = file.read()
        file.close()
        return data

    def write(self, data):
        file = open(self.filepath, 'a')
        file.write(data)
        file.close()

class User:
    def __init__(self, name):
        self.name = name
        self.right_answers = 0
        self.result = ''

    def set_result(self, result):
        self.result = result

    def right_answers_counter(self):
        self.right_answers += 1


class UsersResultsStorage:
    def save(self, user):
        file = open('game_results.txt', 'a')
        file.write(f'{user.name}-{user.right_answers}-{user.result}\n')
        file.close()

    def print_storage(self):
        file = open('game_results.txt', 'r')
        print(f'Имя       кол-во правильных ответов   результат')
        for line in file:
            line_list = line.strip('\n').split('-')
            name = line_list[0]
            right_answers = line_list[1]
            result = line_list[2]
            print(f'{name:10}{right_answers:28}{result}')
        file.close()


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


def validate_user_answer(user_input):
    if not user_input.isdigit():
        print('нужно ввести число')
        return validate_user_answer(input())
    return int(user_input)


questions_storage = QuestionsStorage()
users_results_storage = UsersResultsStorage()


def init_test():
    questions = questions_storage.get_questions()
    total_questions = len(questions)
    print('как вас зовут?')
    user = User(input())

    for i in range(len(questions)):
        random_index = random.randint(0, len(questions) - 1)
        print(f'№{i + 1}. {questions[random_index].text}')
        user_answer = validate_user_answer(input())
        if user_answer == questions[random_index].answer:
            print('test')
            user.right_answers_counter()
        questions.pop(random_index)
    user.set_result(get_result(user.right_answers, total_questions))
    users_results_storage.save(user)
    print(f'Верных ответов: {user.right_answers}. Вы, {user.name} - {user.result}.')
    print('хотите повторить попытку? y/n')
    if input().lower() == 'y':
        init_test()


init_test()
users_results_storage.print_storage()
