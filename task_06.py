num = int(input())
total = 0
counter = 0

while num != 0:
    counter += 1
    total += num
    num = int(input())
if counter != 0:
    print(total / counter)
# нужно ли тут округлять? потому что возвращается всегда float, а в твоем примере в выводе просто 2, а не 2.0