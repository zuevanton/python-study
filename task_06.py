num = int(input())
if num == 0:
    print('зеленый')
elif 0 < num < 11 or 18 < num < 29:
    if num % 2 == 1:
        print('красный')
    else:
        print('черный')
elif 10 < num < 19 or 28 < num < 37:
    if num % 2 == 1:
        print('черный')
    else:
        print('красный')
else:
    print('ошибка ввода')
