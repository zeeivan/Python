first_day = int (input('Спортсмен пробежал в первый день:'))
last_day = int (input('Спортсмен пробежал в последний день:'))
day = int (1)
while first_day <= last_day:
    first_day *= 1.1
    day += 1
    print(day, '-й день:', first_day)
