counter = 0
for i in range(1, int(input()) + 1):
    counter += str(i).count('5')
print(counter)