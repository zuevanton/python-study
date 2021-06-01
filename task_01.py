num = int(input())
words_list = []
for i in range(num):
    words_list.append(input())
print('введите поисковый запрос:', end=' ')
query = input()

for word in words_list:
    if query.lower() in word.lower():
        print(word)