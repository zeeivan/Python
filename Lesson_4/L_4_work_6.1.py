from itertools import cycle

с = 0
for el in cycle("Mikolenko"):
    if с > 15:
        break
    print(el)
    с += 1
