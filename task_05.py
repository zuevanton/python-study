num = int(input())
counter_positive = 0
counter_negative = 0

while num != 0:
    if num > 0:
        counter_positive += num
    else:
        counter_negative += num
    num = int(input())
print(counter_negative * counter_positive)
