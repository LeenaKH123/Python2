# Write a script that takes in a string from the user.
# Using the `split()` method, create a list of all the words in the string
# and print back the most common word in the text.
string_ = input("Please enter your sentence: ")
splitted = string_.split(" ")
print(splitted, "this is the original list from the user")
counts = []
repeated = []
for word in splitted:
    if word not in counts:
        counts.append(word)
print(counts, "list with no repeated words")
for word in splitted:
    if word in repeated:
        print(word, "this word is repeated")
    repeated.append(word)
