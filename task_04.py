num = int(input())
min_digit = num % 10
max_digit = num % 10

while num != 0:
    if num % 10 < min_digit:
        min_digit = num % 10
    if num % 10 > max_digit:
        max_digit = num % 10
    num = num // 10

print('Максимальная цифра равна', max_digit)
print('Минимальная цифра равна', min_digit)
