# Use the union operator `|` to intersect the two given sets
# inside of a set comprehension that squares each item of the
# set if the number is higher than `2`.
# You should write the whole code logic in only one line.
#
# Expected output: {16, 9, 25, 49}
#
# Remember that sets are unordered collections, so your numbers
# might come out in a different order.

s = {1, 2, 3, 4}
t = {2, 3, 4, 5, 7}
# ---working code 1 ----
# union_set = set()
# for itemS in s:
#     for itemT in t:
#         if itemS > 2:            
#             union_set.add(itemS)
#         if itemT > 2:
#             union_set.add(itemT)
# union_set_squared = [number**2 for number in union_set]
# print(union_set_squared)
#-----end of working code 1------
#working code 2
# union_set = s | t
# union_set2 = set()
# for x in union_set:
#     if x>2:
#         union_set2.add(x)
# union_set_squared = [number**2 for number in union_set2]
# print(union_set_squared)
# ---end of working code 2 ---

# union_set = set([number**2 for number in s|t if number > 2 ])
union_set = {number**2 for number in s|t if number > 2}
print(union_set)