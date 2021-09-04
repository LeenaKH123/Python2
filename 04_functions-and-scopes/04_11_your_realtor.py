# Write a function that prints out nicely formatted information about a
# real estate listing. The information can vary for every listing, which
# is why your function should be able to take an arbitrary amount of
# keyword arguments, and display them all in a list form with some
# introductory information.

estate_list = {"NY": "building1", "DC": "building2"}


def estate(**kwargs):
    for k, v in kwargs.items():
        print(k, v)


print("estate information", estate(**estate_list))
