# пример data = [4, 34, 34, 98]
#            что сделать      где взять      при каком условии
# new_list = [item         for item in data  if item > 10]  -  это значит, что сначала мы пишем что нужно сделать с элементом
# (item)(или можно написать item+1000), дальше откуда взять (for item in data) и дальше при каком условии if item > 10.

from math import *  # импорт всех матемитических функций
orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]

new_orbits = [(a,b)  for (a,b) in orbits if a != b]
max_area = [pi* a * b for (a,b) in new_orbits] #находим максимальное значение площади
print(max_area)
print(max_area.index(max(max_area))) #находим индекс максимальной площади
