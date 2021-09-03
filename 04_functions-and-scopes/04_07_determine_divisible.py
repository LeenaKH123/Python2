# Write a script where you complete the following tasks:
# - define a function that determines whether the number is
#   divisible by 4 OR 7 and returns a boolean
# - define a function that determines whether a number is
#   divisible by both 4 AND 7 and returns a boolean
# - take in a number from the user between 1 and 1,000,000,000
# - call your functions, passing in the user input as the arguments,
#   and set their output equal to new variables
# - print your the result variables with descriptive messages


def four_or_seven(number):
    if number % 4 == 0 or number % 7 == 0:
        return True
    return False


def four_and_seven(number):
    if number % 4 == 0 and number % 7 == 0:
        return True
    return False


user_number = int(input("give me number between one and billion "))
output1 = four_or_seven(user_number)
output2 = four_and_seven(user_number)
if output2:
    print("your number is divisible by four and seven")
elif output1:
    print("your number is divisible by four or seven ")
else:
    print("your number is not divisible by four or seven")
