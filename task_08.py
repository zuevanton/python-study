counter = 0
str = input()

for i in range(len(str) - 1):
    if str[i] == str[i + 1]:
        counter += 1
print(counter)