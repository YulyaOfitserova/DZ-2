month = int(input('Введите номер месяца (от 1 до 12): '))
month_list = [12, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

if month in month_list[0:3]:
    print('Это зима')
elif month in month_list[3:6]:
    print('Это весна')
elif month in month_list[6:9]:
    print('Это лето')
else:
    print('Это осень')