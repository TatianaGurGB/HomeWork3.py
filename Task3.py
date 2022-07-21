# Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между 
# максимальным и минимальным значением дробной части элементов.

# Пример:

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

my_list = [1.1, 1.2, 3.1, 5, 10.01]
var = 0
max = 0
min = 1
i = 0

while i < len(my_list):
    var = my_list[i] % 1
    print(round(var, 2))
    i +=1
    if var < min and var != 0:
        min = var
    if var > max and var != 0:
        max = var

dif = max - min
print(f'разность между {round(max, 2)} и {round(min, 2)} равна {round(dif, 2)}')
    
