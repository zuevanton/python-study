num = abs(int(input()))
first_num = num % 1000 // 100
second_num = num % 100 // 10
third_num = num % 10
print('Сумма цифр числа', num, 'равна', first_num + second_num + third_num)
print('Произведение цифр числа', num, 'равно', first_num * second_num * third_num)
