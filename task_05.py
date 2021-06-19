def is_date_starry(date):
    day = int(date.split('.')[0])
    month = int(date.split('.')[1])
    year = int(date.split('.')[2]) % 100
    return True if day * month == year else False


print(is_date_starry(input()))
