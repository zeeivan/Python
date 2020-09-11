user_word = input ('Введите фразу:')
list = list(user_word.rsplit())
for i in range (len(list)):
    print(i+1, list [i])

