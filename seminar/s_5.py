# Хакер Василий получил доступ к классному журналу и хочет заменить все свои 
# минимальные оценки на максимальные. Напишите программу, которая заменяет оценки Василия, 
# но наоборот: все максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4

# Output: 1 3 3 3 1
marks = [1,3,3,3,4]
min_marks = min(marks)
max_marks = max(marks)
for i in range (len(marks)):
    if marks[i] == max_marks:
        marks[i] = min_marks
print(marks)