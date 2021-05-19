flag = 0

for i in range(int(input())):
    if int(input()) % 2 == 0:
        flag = 1
if flag:
    print('NO')
else:
    print('YES')
