numbers = input().split()
counter = 0
for i in numbers:
    for j in numbers:
        if i == j:
            counter += 1
    counter -= 1
print(counter / 2)