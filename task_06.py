num = int(input())
first_num = num % 10000 // 1000
second_num = num % 1000 // 100
third_num = num % 100 // 10
fourth_num = num % 10
print('У числа', num, 'максимальная цифра равна', max(first_num, second_num, third_num, fourth_num))
