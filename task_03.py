total = 0
num = int(input())
num_temp = num
while num_temp != 0:
    total += num_temp % 10
    num_temp = num_temp // 10

if num % total == 0:
    print('YES')
else:
    print('NO')
