word = input('Введите строку из нескольких слов, разделенных пробелами: ')
word = [str(x) for x in word.split()]

if len(str(word)) <= 10:
    for ind, el in enumerate(word, 1):
        print(ind, el)
else:
    for ind, el in enumerate(word, 1):
        print(ind, el[0:10])
