# CHALLENGE: Write a script that sorts a dictionary into a
# list of tuples based on the dictionary's values. For example:

# input_dict = {"item1": 5, "item2": 6, "item3": 1}
# result_list = [("item3", 1), ("item1", 5), ("item2", 6)]

# Check out the Python docs and see whether you can come up with a solution,
# even if you don't yet completely understand why it works the way it does:
# https://docs.python.org/3/howto/sorting.html#key-functions
# Feel free to discuss any questions you have with your mentor and on the forum!
<<<<<<< HEAD
input_dict = {"item1": 5, "item2": 6, "item3": 1}
items_ = sorted(input_dict.items())
sortedbykey = {k: v for k, v in sorted(input_dict.items())}
sortedbyvalue = {k: v for k, v in sorted(input_dict.items(), key=lambda v: v[1])}
print(sortedbykey)
print(sortedbyvalue)
=======

input_dict = {"item1": 5, "item2": 6, "item3": 1}
items_ = sorted(input_dict.items())
sortedbykey = {k:v for k, v in sorted(input_dict.items())}
sortedbyvalue = {k:v for k, v in sorted(input_dict.items(), key = lambda v:v[1])}
print(sortedbykey)
print(sortedbyvalue)
  
>>>>>>> 6c32bfe7980fffb160c8a3c13ccab51d4242e643
