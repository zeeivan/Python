def my_func(x, y):
    if y == 0:
        return 1
    else:
        return x * my_func(x, 1 - y)


print(my_func(float(input()), int(input())))
