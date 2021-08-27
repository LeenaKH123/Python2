# Write code that creates a list of all unique values in a list.
# For example:
#
# list_ = [1, 2, 6, 55, 2, 'hi', 4, 6, 1, 13]
# unique_list = [55, 'hi', 4, 13]
list_ = [1, 2, 6, 55, 2, "hi", 4, 6, 1, 13]
unique_list = []
for x in list_:
    if x not in unique_list:
        unique_list.append(x)
    for x in unique_list:
        print(x),

print("the unique values from list is", unique_list)
