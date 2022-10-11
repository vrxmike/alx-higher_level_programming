#!/usr/bin/python3
list_division = __import__('4-list_division').list_division

my_1_1 = [10, 8, 4]
my_1_2 = [2, 4, 4]
result = list_division(my_1_1, my_1_2, max(len(my_1_1), len(my_1_2)))
print(result)

print("--")

my_1_1 = [10, 8, 4, 4]
my_1_2 = [2, 0, "H", 2, 7]
result = list_division(my_1_1, my_1_2, max(len(my_1_1), len(my_1_2)))
print(result)
