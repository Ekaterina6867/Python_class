# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
N = int(input('Введите количество элементов списка А: '))
Enter = input("Введите через пробел элементы списка: ").split()
List_1 = list(map(int, Enter))
if len(List_1) != N:
    print('Введенные элементы не соответствуют заявленному количеству')
else:
    X = int(input('Введите число X: '))
    count = 0
    for i in range(N):
        if List_1[i] == X:
            count += 1
    print(f'Число {X} встречается в списке A {count} раз') 