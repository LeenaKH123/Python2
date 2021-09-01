# Using f-strings, print out the name, last name, and favorite
# office supply item of each person in the given dictionary,
# formatted like so:
#
# LASTNAME, Name           Office supply item
# LONGERLASTNAME, Name     Office supply item

office = [
    {"full_name": "Michael Scott", "item": "world's best boss mug"},
    {"full_name": "Dwight Schrute", "item": "pepper spray"},
    {"full_name": "Jim Halpert", "item": "phone"},
    {"full_name": "Pam Beesly", "item": "post-its"},
    {"full_name": "Ryan Howard", "item": "business cards"},
    {"full_name": "Stanley Hudson", "item": "crossword-puzzle"},
    {"full_name": "Kevin Malone", "item": "m&ms"},
    {"full_name": "Meredith Palmer", "item": "flask"},
    {"full_name": "Angela Martin", "item": "cat food"},
    {"full_name": "Oscar Martinez", "item": "calculator"},
    {"full_name": "Phyllis Lapin", "item": "cut flowers"},
    {"full_name": "Kelly Kapoor", "item": "People magazine"},
    {"full_name": "Toby Flenderson", "item": "files"},
    {"full_name": "Creed Bratton", "item": "mung beans"},
    {"full_name": "Darryl Philbin", "item": "forklift"},
]
for dictionary in office:
    full_name = dictionary["full_name"]
    item = dictionary["item"]
    list_ = full_name.split(" ")
    if len(list_) == 3:
        first_name = list_[0] + " " + list_[1]
        last_name = list_[2]
    else:
        first_name = list_[0]
        last_name = list_[1]

    # "The inspiring quote" - Lastname, Firstname
    # print(f"Hello {name}. Next year you'll be {age + 1}!")
    print(f"{last_name}, {first_name}      {item}")
