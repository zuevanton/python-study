char_num = ord(input())
if ord('a') <= char_num <= ord('z'):
    print(chr(char_num).upper())
elif ord('A')<= char_num <= ord('Z'):
    print(chr(char_num).lower())
else:
    print(chr(char_num))
