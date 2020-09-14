example_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
#sort_list=sorted(example_list)
#sort_list=[2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
#print(sort_list)
final_list = [el for el in example_list if example_list.count(el) < 2]
print('Лист без повторяющихся значений', final_list)
