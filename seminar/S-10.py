
# задача скопировать список
values = [1,23,42, 'dkl']
transormed_values = list(map(lambda items: items, values)) #лямбда принимает аргумент из value и возвращает его
if values == transormed_values:
    print('ok')
else:
    print('fals')    