time = int (input('Введите время в секундах:'))
hours = time // 3600
minutes = (time % 3600)//60
secondes = ((time % 3600)%60)
print (hours, ':', minutes, ':', secondes)