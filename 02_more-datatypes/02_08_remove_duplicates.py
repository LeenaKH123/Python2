# Write code that removes all duplicates from a list.
# Solve this challenge in two ways:
# 1. Convert to a different data type
# 2. Use a loop and a second list to solve it more manually

list_ = [1, 2, 3, 4, 3, 4, 5]
list_ = [1, 2, 3, 4, 1, 4, 3, 4, 5]
result = []
for char in list_:
    if char in result:
        print(char, "is a duplicate")
    else:
        result.append(char)
print(result, "here is the list without duplication")
# convert to a different data type
print(set(list_))
