# Write a script that takes the following two dictionaries
# and creates a new dictionary by combining the common keys
# and adding the values of duplicate keys together.
# Use `for` loops to iterate over these dictionaries
# to accomplish this task.
#
# Example output:
# result = {"a": 3, "b": 2, "c": 7 , "d": 2}

dict_1 = {"a": 1, "b": 2, "c": 3}
dict_2 = {"a": 2, "c": 4, "d": 2}
dd = {}
for d in (dict_1, dict_2):
    for key, value in d.items():
        if key in dd:
            dd[key] = dd[key] + value
        else:
            dd[key] = value
print(dd)
