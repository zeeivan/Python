from functools import reduce
my_list = [i for i in range(99, 1001) if i%2==0]
def my_func(prev_el, el):
           return prev_el * el
print(reduce(my_func, my_list))
