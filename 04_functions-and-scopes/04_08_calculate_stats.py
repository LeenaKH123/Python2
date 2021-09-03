# Write a function named `stats()` that takes in a list of numbers
# and finds the maximum, minimum, average and sum of the numbers.
# Print these values to the console you call the function.

example_list = [1, 2, 3, 4, 5, 6, 7]
minimum = 0
maximum = 0
average = 0
total = 0
counter = 0


def stats(example_):
    for num in example_:
        total = total + num
        counter = counter + 1
        if num > maximum:
            maximum = num
        else:
            minimum = num

        average = total / counter
        print("maximum", maximum)
        print("minimum", minimum)
        print("average", average)


print(stats(example_list))

# call the function below here
