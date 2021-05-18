stopwatch = int(input())
hours = stopwatch // 60 // 60
minutes = stopwatch // 60 - hours * 60
seconds = stopwatch % 60
print(stopwatch, 'секунд - это', hours, 'час', minutes, 'минут', seconds, 'сек')
