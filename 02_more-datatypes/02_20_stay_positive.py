# Use a list comprehension to create a list called `positive` from the list
# `numbers` that contains only the positive numbers from the provided list.

numbers = [5, -8, 3, 10, -19, -22, 44, 2, -1, 4, 42]
# numbers = [5, -8, 3, 10, -19, -22, 44, 2, -1, 4, 42]
list_ = []
for num in numbers:
    if num > 0:
        list_.append(num)
print(list_)
