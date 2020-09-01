month = int(input('Введите номер месяца'))
time_of_years = ['winter', 'spring', 'summer', 'autumn']
if month == 1 or month ==  2 or month == 12:
    print (time_of_years[0])
elif month == 3 or month ==  4 or month == 5:
    print(time_of_years[1])
elif month == 6 or month == 7 or month == 8:
    print(time_of_years[2])
elif month == 9 or month == 10 or month == 11:
    print(time_of_years[3])
else:
    print (month, "месяца в году не существует!")

