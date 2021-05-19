ticket = input()
num = int(ticket)
left_num = num // 1000
right_num = num % 1000
sum_left_num = left_num // 100 % 10 + left_num // 10 % 10 + left_num % 10
sum_right_num = right_num // 100 % 10 + right_num // 10 % 10 + right_num % 10
if sum_right_num == sum_left_num:
    print('Билет', ticket, 'счастливый')
else:
    print('Билет', ticket, 'НЕсчастливый')
