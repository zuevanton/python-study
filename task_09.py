flag = 0

for i in range(int(input())):
    if int(input()) % 2 == 1:
        flag = 1
if flag:
    print('YES')
else:
    print('NO')
