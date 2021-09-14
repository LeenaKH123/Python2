# Demonstrate how to create a generator object.
# Print the object to the console to see what you get.
# Then iterate over the generator object and print out each item.
generator = (x*2 for x in range(5))
print(generator)
for x in generator:
    print(x)
