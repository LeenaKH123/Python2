# Write a function named `stats()` that takes in a list of numbers
# and finds the maximum, minimum, average and sum of the numbers.
# Print these values to the console you call the function.

example_list = [1, 2, 3, 4, 5, 6, 7]


def stats(example_):
    total = 0
    counter = 0
    minimum = float("inf")
    maximum = 0
    average = 0
    for num in example_:
        total = total + num
        counter = counter + 1
        if num > maximum:
            maximum = num
        if num < minimum:
            minimum = num
    average = total / counter
    print("maximum", maximum)
    print("minimum", minimum)
    print("average", average)
    print("sum", total)


print(stats(example_list))

# call the function below here
