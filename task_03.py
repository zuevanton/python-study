num = int(input())
flag = 'NO'
while num != 0:
    if num % 10 == 1:
        flag = 'YES'
        break
    num //= 10
print(flag)