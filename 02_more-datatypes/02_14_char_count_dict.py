# Write a script that takes a text input from the user
# and creates a dictionary that maps the letters in the string
# to the number of times they occur. For example:
#
# user_input = "hello"
# result = {"h": 1, "e": 1, "l": 2, "o": 1}
x = input("type your string without spaces ")
freq = {}
for c in set(x):
    freq[c] = x.count(c)
print(freq)
