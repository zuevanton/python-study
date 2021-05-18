num = int(input())
last_three_num = num % 1000
first_num = last_three_num // 100
second_num = last_three_num // 10 % 10
third_num = last_three_num % 10
print('У числа', num, 'сумма последних трех цифр равна', first_num + second_num + third_num)
