a = int(input())
b = int(input())
if a > b:
    temp = a
    a = b
    b = temp
for i in range(a, b + 1):
    print(i)
