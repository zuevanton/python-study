num = int(input())
if num == 1:
    print('yes')
else:
    divider = 2
    while num % divider != 0:
        divider += 1
    if num == divider:
        print('yes')
    else:
        print('no')