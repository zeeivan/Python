from math import  factorial
generator = (param * param for param in range(5))

for el in generator:
    print(el)