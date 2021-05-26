num = int(input())

for i in range(1, num + 1):
    if 2 <= i <= 8 or 128 <= i <= 256 or 1024 <= i <= 2048:
        continue
    print(i)
