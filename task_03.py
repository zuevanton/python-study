def get_month_days(month_number):
    if month_number > 12:
        return
    months_with_31 = [1, 3, 5, 7, 8, 10, 12]
    if month_number in months_with_31:
        return 31
    elif month_number == 2:
        return 28
    else:
        return 30


print(get_month_days(int(input())))