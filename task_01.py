def count_rank(num):
    rank = 0
    while num > 0:
        rank += 1
        num = num // 10
    return rank

print('test')
print(count_rank(int(input())) * count_rank(int(input())))
