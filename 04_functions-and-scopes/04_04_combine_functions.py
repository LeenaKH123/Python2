# Combine the `greet()` function that you developed in the course materials
# with the `write_letter()` function from the previous exercise.
# Write both functions in this script and call `greet()` within `write_letter()`
# to let `greet()` take care of creating the greeting string.


def say_hello(name):
    #     return print(f"Hello {name}!")
    return f"Hello {name}!"


def write_letter(name, text):
    greeting = say_hello(name)
    goodbye = f"bye bye {name}"
    letter = f"{greeting} , {text}, {goodbye}"
    return letter


print(write_letter("Mary", "functions2"))
