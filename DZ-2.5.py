rating = int(input('Введите значение рейтинга (целое число): '))
my_list = [7, 5, 3, 3, 2]

for elem in my_list:
    if rating > elem:
        ind = my_list.index(elem)
        my_list.insert(ind, rating)
        break

    elif rating <= min(my_list):
        my_list.append(rating)
        break

print(my_list)
