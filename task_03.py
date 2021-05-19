text_1 = input()
text_2 = input()
text_3 = input()
max_symbols = max(len(text_1), len(text_2), len(text_3))
if len(text_1) == max_symbols:
    print(text_1)
elif len(text_2) == max_symbols:
    print(text_2)
else:
    print(text_3)
