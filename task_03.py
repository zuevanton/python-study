ip = input()
flag = 0
for num in ip.split('.'):
    if not 0 <= int(num) <= 255:
        flag = 1

if flag:
    print('NO')
else:
    print('YES')
