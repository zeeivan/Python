#example_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
#final_list = [el for num in example_list if el[0] < el[0+1]]
#print (final_list)


example_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
final_list = [el for num, el in enumerate(example_list) if example_list[num-1] < example_list[num]]
print('Новый список', final_list)
