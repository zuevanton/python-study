import math

maximum = 0
# т.к. любое натуральное больше 0, то на первой итерации цикла мы перезапишем maximum
minimum = math.inf
# тут в первой итерации перезапишем minimum, т.к. любое число меньше бесконечности
# да, можно было сначала вне цикла первое введенное число записать в minimum и maximum
# и прогонять цикл на одну итерацию меньше, но решил так сделать :)

for i in range(int(input())):
    number = int(input())
    if number < minimum:
        minimum = number
    if number > maximum:
        maximum = number
print('Минимум равен', minimum)
print('Максимум равен', maximum)
