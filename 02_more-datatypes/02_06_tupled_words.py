# Write a script that takes a string from the user
# and creates a list that contains a tuple for each word.
# For example:

# input = "hello world"
# result_list = [('h', 'e', 'l', 'l', 'o'), ('w', 'o', 'r', 'l', 'd')]
usersay = input("Enter your senetnce ")
userlist = usersay.split(" ")
result = []
for char in userlist:
    char = tuple(char)
    result.append(char)
print(result)
