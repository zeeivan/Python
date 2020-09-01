gain = int (input('Введите выручку'))
cost = int (input ('Ведите затраты'))
profit = gain - cost
if gain > cost:
    print ('Фирма работает с прибылью', profit)
    print ('Рентабельность составила:', profit / gain)
    population = int (input ('Введите численность сотрудников'))
    print('Выручка на одного работника:', profit/population)
elif gain < cost:
    print ('Фирма работает с убытком', profit)