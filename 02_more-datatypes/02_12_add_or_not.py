# MEMORY GAME WITH SETS
# Continuously collect number input from a user with a `while` loop.
# Confirm that the input can be converted to an integer,
# then add it to a Python `set()`.
# If the element was already in the set, notify the user that their
# input hasn't been added and deduce a point.
# If the user gets loses 5 points, quite the program.
# They will win if they manage to create a set that has more than 10 items.


user_set = set({})
win = False
points = 0
while not win:
    user_input = input("please type a number ")
    user_input_int = int(user_input)
    if user_input_int in user_set:
        points -= 1
        print("your number is not added and you lost a point")
        print("you currently have ", points)
        if points == -5:
            print("you lost")
            break
    else:
        user_set.add(user_input_int)
        if len(user_set) > 10:
            win = True
            print("You won!")
