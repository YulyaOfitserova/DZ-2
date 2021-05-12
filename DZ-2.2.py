elem = input('Введите элементы для списка через пробел: ')
my_list = [x for x in elem.split()]
num = int(len(my_list))

if num % 2 == 0:
    my_list[::2], my_list[1::2] = my_list[1::2], my_list[::2]

else:
    n = num - 1
    my_list[:n:2], my_list[1:n:2] = my_list[1:n:2], my_list[:n:2]

print(my_list)