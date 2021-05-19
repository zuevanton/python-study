counter = 0
num = int(input())
while num % 10 != 0:
    if num % 10 == 5:
        counter += 1
    num = num // 10
print(counter)
