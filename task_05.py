char_num_1 = ord(input())
char_num_2 = ord(input())

for c in range(min(char_num_1, char_num_2), max(char_num_1, char_num_2) + 1):
    print(chr(c))
