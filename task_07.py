total = 1
for i in range(1, int(input()) + 1):
    if i % 10 == 2 or i % 10 == 9:
        total *= i
if total == 1:
    total = 0
print(total)
