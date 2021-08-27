# Using f-strings, print out the name, last name,
# and quote of each person in the given dictionary,
# formatted like so:
#
# "The inspiring quote" - Lastname, Firstname

# name = "Tom"
# age = 99

# print(f"Hello {name}. Next year you'll be {age + 1}!")

famous_quotes = [
    {
        "full_name": "Isaac Asimov",
        "quote": "I do not fear computers. I fear lack of them.",
    },
    {
        "full_name": "Emo Philips",
        "quote": "A computer once beat me at chess, but it was no match for me at "
        "kick boxing.",
    },
    {
        "full_name": "Edsger W. Dijkstra",
        "quote": "Computer Science is no more about computers than astronomy "
        "is about telescopes.",
    },
    {
        "full_name": "Bill Gates",
        "quote": "The computer was born to solve problems that did not exist before.",
    },
    {
        "full_name": "Norman Augustine",
        "quote": "Software is like entropy: It is difficult to grasp, weighs nothing, "
        "and obeys the Second Law of Thermodynamics; i.e., it always increases.",
    },
    {
        "full_name": "Nathan Myhrvold",
        "quote": "Software is a gas; it expands to fill its container.",
    },
    {
        "full_name": "Alan Bennett",
        "quote": "Standards are always out of date.  That’s what makes them standards.",
    },
]

for dictionary in famous_quotes:
    quote = dictionary["quote"]
    full_name = dictionary["full_name"]
    list_ = full_name.split(" ")
    if len(list_) == 3:
        first_name = list_[0] + " " + list_[1]
        last_name = list_[2]
    else:
        first_name = list_[0]
        last_name = list_[1]

    # "The inspiring quote" - Lastname, Firstname
    # print(f"Hello {name}. Next year you'll be {age + 1}!")
    print(f'"{quote}" - {last_name}, {first_name}')
