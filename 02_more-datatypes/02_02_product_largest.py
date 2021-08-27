# Take in 10 numbers from the user. Place the numbers in a list.
# You can also use the provided random `randlist` list
# to simulate user input.
# Find the largest number in the list and print the result.
# Calculate the product of all of the numbers in the list.

from resources import randlist

print(randlist)
import random

randlist = []
for i in range(0, 10):
    num = random.randint(1, 30)
    randlist.append(num)
print(randlist)
randlist.sort()
print(randlist)
print("Largest number in the list is:", randlist[-1])
result = 1
for x in randlist:
    result = result * x
print("the product of all the numbers in the list is", result)
