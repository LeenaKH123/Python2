# Using a list comprehension, create a *cartesian product* (google this!)
# of the given lists. Then open up your online shop ;)

colors = ["neon orange", "spring green"]
sizes = ["S", "M", "L"]
# [ (i,j) for i in range(1,3) for j in range(1,5) ]
colors_sizes = [(color,size) for color in colors for size in sizes]
print(colors_sizes)