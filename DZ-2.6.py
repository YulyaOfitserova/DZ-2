name = input('Введите названия товаров через пробел: ')
price = input('Введите цену каждого товара из списка выше через пробел: ')
count = input('Введите количество каждого товара из списка выше через пробел: ')
unit = input('Введите единицы измерения для товаров из списка через пробел: ')

name = [str(x) for x in name.split()]
price = [str(x) for x in price.split()]
count = [str(x) for x in count.split()]
unit = [str(x) for x in unit.split()]

num = 1
ind = 0
count_elem = len(name)

while ind < count_elem:
    my_dict = {'название': name[ind], 'цена': price[ind], 'количество': count[ind], 'ед': unit[ind]}
    my_tuple = (num, my_dict)
    print(my_tuple)
    num += 1
    ind += 1

print("Аналитика товаров: ")
dict_all = {'название': name, 'цена': price, 'количество': count, 'ед': unit}
for k, v in dict_all.items():
    print(k, ':', v)
