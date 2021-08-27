# The import below gives you a new random list of numbers,
# called `randlist`, every time you run the script.
#
# Write a script that takes this list of numbers and:
#     - sorts the numbers
#     - stores the numbers in tuples of two in a new list
#     - prints each tuple
#
# If the list has an odd number of items,
# add the last item to a tuple together with the number `0`.
#
# Note: This lab might be challenging! Make sure to discuss it
# with your mentor or chat about it on our forum.

from resources import randlist

print(randlist)

# Write your code below here
import random

randlist = []
for i in range(0, 10):
    num = random.randint(1, 30)
    randlist.append(num)
print(randlist)
randlist.sort()
print(randlist)
# lst_tuple = [x for x in zip(*[iter(randlist)])]
# print(lst_tuple)
lst_tuple = [x for x in zip(*[iter(randlist)] * 2)]
print(lst_tuple)
